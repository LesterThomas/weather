# Typescript MCP example

Following instructions at https://github.com/modelcontextprotocol/typescript-sdk


Install the required modules

```
npm install @modelcontextprotocol/sdk
```

Build the Typescript to Javascript

```
npm run build
```

This will build the Javascript MCP server in `/typescript/build/index.js`


## Adding to MCP Client

Open the config file for the client (e.g. for Claude Desktop, this is in $env:AppData\Claude\claude_desktop_config.json).

Add the following MCP Server:

```json

{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": [
          "PATH TO/weather/typescript/build/index.js"
      ]
    }    
  }
}

```

## Example Prompt Templates

### Weather Alerts by State
Use this prompt template to get current weather alerts for a specific US state:

```
I need to know about any weather alerts or warnings in [STATE].
Can you check the current alerts for me using the weather tool?
```

Example:
```
I need to know about any weather alerts or warnings in California.
Can you check the current alerts for me using the weather tool?
```

### Weather Forecast by Location
Use this prompt template to get a detailed weather forecast for a specific location:

```
What's the weather forecast for [CITY NAME] at coordinates [LATITUDE], [LONGITUDE]?
Please provide details about temperature and conditions.
```

Example:
```
What's the weather forecast for San Francisco at coordinates 37.7749, -122.4194?
Please provide details about temperature and conditions.
```

### Trip Planning
You can also combine both tools in a single conversation:

```
I'm planning a trip to [STATE] and will be staying near coordinates [LATITUDE], [LONGITUDE].
Are there any weather alerts I should be aware of in the state? 
And what's the forecast for my specific location for the next few days?
```

Note: This MCP server only provides data for locations within the United States as it uses the National Weather Service API.
