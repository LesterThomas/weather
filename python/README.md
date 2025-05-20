# MCP server PoC for Weather

## Installation

These instructions are based on https://modelcontextprotocol.io/quickstart/server

Install uv

MacOS/Linux
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


Set-up the project using uv

MacOS/Linux
```
# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx
```

Windows
```
# Create virtual environment and activate it
uv venv
.venv\Scripts\activate

# Install dependencies
uv add mcp[cli] httpx
```


Run the MCP server using

```
uv run weather.py
```



Add the following config to your MCP Client (tested in Claude Desktop and VSCode):

```
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/python/mcp-weather",
                "run",
                "weather.py"
            ]
        }
    }
}
```

## Example Prompt Templates

### Weather Alerts by State
To get current weather alerts and warnings for a specific US state:

```
What are the current weather alerts for [STATE]?
Please use the weather tool to check for any active alerts or warnings.
```

Example:
```
What are the current weather alerts for TX?
Please use the weather tool to check for any active alerts or warnings.
```

### Weather Forecast by Location
To get a detailed forecast for a specific location by coordinates:

```
I need a weather forecast for [LOCATION NAME] at latitude [LATITUDE] and longitude [LONGITUDE].
Can you tell me the temperature, wind conditions, and general forecast?
```

Example:
```
I need a weather forecast for Miami at latitude 25.7617 and longitude -80.1918.
Can you tell me the temperature, wind conditions, and general forecast?
```

### Trip Planning
For planning trips with multiple locations:

```
I'm planning a trip to [STATE] and will be visiting several locations:
- [LOCATION 1] at coordinates [LAT1], [LONG1]
- [LOCATION 2] at coordinates [LAT2], [LONG2]

Are there any weather alerts in the state I should know about?
What's the forecast for each of these locations?
```

Note: The National Weather Service API used by this MCP server only provides data for locations within the United States.