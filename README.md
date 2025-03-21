# MCP Server POC

A proof-of-concept implementation of a Model Context Protocol (MCP) server for enhancing AI assistant capabilities with custom tools and resources.

## Overview

This project demonstrates how to create and use a Model Context Protocol (MCP) server that can provide custom tools and resources to AI assistants like Claude and others that support the MCP standard. The server includes:

- Simple math operations (addition)
- Dynamic greeting resource
- Web crawling capability using the crawl4ai library

## Requirements

- Python 3.8+
- Required packages:
  - mcp
  - crawl4ai

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/mcp-server-poc.git
cd mcp-server-poc
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

To run the MCP server directly:

```bash
python first-mcp.py
```

The server will start and wait for connections using the stdio transport method.

### Integrating with Cursor

To use this MCP server with Cursor IDE:

1. Create or edit the file `~/.cursor/mcp.json` (on Windows: `C:\Users\<username>\.cursor\mcp.json`) with the following content (alternatively, copy and edit the included `sample_mcp.json` file):

```json
{
    "mcpServers": {
        "mcp-server": {
            "command": "uv", 
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/YOUR/mcp-server",
                "run",
                "main.py"
            ]
        }
    }
}
```

2. Replace the path with the absolute path to your `first-mcp.py` file.
   - On Windows, use double backslashes: `C:\\Users\\username\\path\\to\\first-mcp.py`
   - On macOS/Linux, use regular slashes: `/Users/username/path/to/first-mcp.py`

3. Restart Cursor completely (including ending any background processes) to load the MCP server.

## Features

### Tools

- **add(a, b)**: Adds two numbers and returns the result
- **crawl_web(url)**: Crawls a given URL and returns the content as markdown

### Resources

- **greeting://{name}**: Returns a personalized greeting for the provided name

## Technical Details

### Windows Binary Mode Fix

This server includes a specific fix for Windows to ensure proper operation with stdio transport:

```python
# Set binary mode for stdin/stdout on Windows
if os.name == 'nt':
    import msvcrt
    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
```

This fix is necessary because Windows distinguishes between text and binary modes for file handling, which can cause issues with the stdio transport mechanism used by MCP.

## Troubleshooting

If you encounter issues with the MCP server:

### Windows-Specific Issues

- **"Failed to create client" or "Client closed" errors**:
  - Make sure to use the binary mode fix included in the server
  - Use the absolute path with double backslashes in the mcp.json configuration
  - Try running the MCP server directly to see if it produces any error output
  - Completely exit Cursor (including terminating any background processes via Task Manager) before restarting

### General Issues

- Verify that all required packages are installed (`pip list` to check)
- Check that the absolute path in the configuration file is correct
- Make sure the MCP server is running with the proper version of Python (same one where packages are installed)
- Try reinstalling the MCP package: `pip uninstall mcp && pip install mcp`

## Sample Files

This repository includes:

- `first-mcp.py`: The main MCP server implementation
- `requirements.txt`: List of required Python packages
- `sample_mcp.json`: Example configuration for Cursor integration

## License

[MIT License](LICENSE)

## Acknowledgements

- This project uses the [Model Context Protocol](https://modelcontextprotocol.io/) SDK
- Web crawling functionality provided by [crawl4ai](https://github.com/crawler-project/crawl4ai)
