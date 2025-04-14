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

