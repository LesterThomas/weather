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