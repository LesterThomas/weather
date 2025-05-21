from typing import Any, List, Dict
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get active weather alerts and warnings for a US state using the National Weather Service API.
    
    Fetches and returns detailed information about current severe weather conditions,
    natural disasters, and other emergency information for the specified state.
    
    Args:
        state: Two-letter US state code (e.g. CA for California, NY for New York)
        
    Returns:
        Formatted text with alert details including event type, affected area, 
        severity, description and instructions
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get detailed weather forecast for a specific location using the National Weather Service API.
    
    Fetches and returns temperature, wind conditions, and forecast information for
    the next several time periods (day and night). 
    
    Args:
        latitude: Latitude of the location in decimal degrees (-90 to 90)
        longitude: Longitude of the location in decimal degrees (-180 to 180)
        
    Returns:
        Formatted text with forecast details for the next 5 periods
        
    Note:
        This API only works for locations within the United States.
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')


# Example prompt templates
@mcp.prompt(name="alert_by_state", description="Get current weather alerts for a specific US state")
def alert_by_state(state: str) -> List[Dict[str, Any]]:
    """Generate a prompt for getting weather alerts by state code.
    
    Args:
        state: Two-letter US state code (e.g. CA for California, TX for Texas)
        
    Returns:
        A prompt template to check for active weather alerts
    """
    return [
        {
            "role": "user",
            "content": f"""What are the current weather alerts for {state}?
Please use the weather tool to check for any active alerts or warnings."""
        }
    ]

@mcp.prompt(name="forecast_by_location", description="Get weather forecast for a specific location by coordinates")
def forecast_by_location(location_name: str, latitude: float, longitude: float) -> List[Dict[str, Any]]:
    """Generate a prompt for getting weather forecast by coordinates.
    
    Args:
        location_name: Name of the location (for reference only)
        latitude: Latitude of the location in decimal degrees
        longitude: Longitude of the location in decimal degrees
        
    Returns:
        A prompt template to get the detailed weather forecast for a location
    """
    return [
        {
            "role": "user",
            "content": f"""I need a weather forecast for {location_name} at latitude {latitude} and longitude {longitude}.
Can you tell me the temperature, wind conditions, and general forecast?"""
        }
    ]

@mcp.prompt(name="trip_planning", description="Get weather alerts and forecasts for a planned trip")
def trip_planning(state: str, locations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Generate a prompt for planning a trip with multiple locations.
    
    Args:
        state: Two-letter US state code for the trip state
        locations: List of locations with their names and coordinates
        
    Returns:
        A prompt template to check weather alerts and forecasts for a trip
    """
    # Format locations for the prompt
    location_text = ""
    for loc in locations:
        location_text += f"- {loc['name']} at coordinates {loc['latitude']}, {loc['longitude']}\n"
    
    return [
        {
            "role": "user",
            "content": f"""I'm planning a trip to {state} and will be visiting several locations:
{location_text}
Are there any weather alerts in the state I should know about?
What's the forecast for each of these locations?"""
        }
    ]
    