# MCP Server POC

A proof-of-concept implementation of a Model Context Protocol (MCP) server for enhancing AI assistant capabilities with custom tools and resources.

## Overview

This project demonstrates how to create and use a Model Context Protocol (MCP) server that can provide custom tools and resources to AI assistants like Claude and others that support the MCP standard. The server includes:

- Documentation search tool for LangChain, LlamaIndex, and OpenAI
- Web crawling capability
- Integration with Google Search API

## Requirements

- Python 3.11
- Required packages listed in requirements.txt

## Installation and Setup

1. Clone this repository:

```bash
git clone https://github.com/yourusername/mcp-server-poc.git
cd mcp-server-poc
```

2. Create and activate a virtual environment:

```bash
# Create a Python 3.11 virtual environment
python -m venv venv

# Activate on Windows
 .\venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

   Create a `.env` file in the root directory with the following:

```
SERPER_API_KEY=your_serper_api_key_here
```

## Running the Application

To run the MCP server:

```bash
python main.py
```

The server will start and wait for connections using the stdio transport method.

## Integrating with Cursor

To use this MCP server with Cursor IDE:

1. Create or edit the file `~/.cursor/mcp.json` (on Windows: `C:\Users\<username>\.cursor\mcp.json`) with the following content:

```json
{
    "mcpServers": {
        "mcp-server": {
            "command": "python", 
            "args": [
                "ABSOLUTE/PATH/TO/main.py"
            ]
        }
    }
}
```

2. Replace the path with the absolute path to your `main.py` file.
   - On Windows, use double backslashes: `C:\\Users\\username\\path\\to\\main.py`
   - On macOS/Linux, use regular slashes: `/Users/username/path/to/main.py`

3. Restart Cursor completely (including ending any background processes) to load the MCP server.

## Features

### Tools

- **get_docs(query, library)**: Searches the documentation for the specified library (langchain, llama-index, or openai) and returns relevant information

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
- Make sure the MCP server is running with the proper version of Python (3.11)
- Verify that your `.env` file contains the required API key
- Try reinstalling the MCP package: `pip uninstall mcp && pip install mcp`

## License

[MIT License](LICENSE)

## Acknowledgements

- This project uses the [Model Context Protocol](https://modelcontextprotocol.io/) SDK
- Web crawling functionality provided by [crawl4ai](https://github.com/crawler-project/crawl4ai)
