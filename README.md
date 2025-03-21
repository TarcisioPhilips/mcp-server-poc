# MCP Server POC

A proof-of-concept implementation of a Model Context Protocol (MCP) server for enhancing AI assistant capabilities with custom tools and resources.

## Overview

This project demonstrates how to create and use a Model Context Protocol (MCP) server that can provide custom tools and resources to AI assistants like Claude and others that support the MCP standard. The server includes:

- Simple math operations (addition)
- Dynamic greeting resource
- Web crawling capability

## Requirements

- Python 3.8+
- Required packages (listed in requirements.txt)

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

### Integrating with Cursor

To use this MCP server with Cursor IDE:

1. Create or edit the file `~/.cursor/mcp.json` with the following content:

```json
{
  "mcpServers": {
    "fastmcp": {
      "command": "python",
      "args": [
        "path/to/your/first-mcp.py"
      ]
    }
  }
}
```

2. Replace `path/to/your/first-mcp.py` with the absolute path to your `first-mcp.py` file.
3. Restart Cursor to load the MCP server.

## Features

### Tools

- **add(a, b)**: Adds two numbers and returns the result
- **crawl_web(url)**: Crawls a given URL and returns the content as markdown

### Resources

- **greeting://{name}**: Returns a personalized greeting for the provided name

## Troubleshooting

If you encounter issues with the MCP server on Windows:

- The server adds specific code to handle binary mode for stdin/stdout on Windows
- Make sure you're using the correct absolute path in your configuration file
- Some clients may require you to manually terminate and restart them to pick up configuration changes

## License

[MIT License](LICENSE)

## Acknowledgements

- This project uses the [Model Context Protocol](https://modelcontextprotocol.io/) SDK
- Web crawling functionality provided by [crawl4ai](https://github.com/crawler-project/crawl4ai)
