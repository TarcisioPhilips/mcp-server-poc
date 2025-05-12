# MCP Note Taker (POC)

A proof-of-concept implementation of a Model Context Protocol (MCP) server for AI assistant note-taking, featuring custom tools and resources for managing notes.

## Overview

This project demonstrates how to create and use a Model Context Protocol (MCP) server that provides note-taking capabilities to AI assistants (such as Claude, Cursor, and others supporting MCP). The server includes:

- A tool to add notes
- A resource to fetch the latest note
- A prompt to summarize all notes

All notes are stored in a local `notes.txt` file in the project directory.

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
# Init uv package manager 
uv init

# Create a Python 3.11 virtual environment
uv venv

# Activate on Windows
 .venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

3. Install the required packages:

```bash
uv pip install -r requirements.txt
```

4. (Optional) Install MCP CLI tools if needed for development or alternative integrations:

```bash
uv add "mcp[cli]"
```

## Running the Application

To run the MCP server:

```bash
uv run mcp
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

- **add_note(note: str)**: Adds a note to the `notes.txt` file and returns a confirmation message.

### Resources

- **notes://latest**: Returns the latest note from the `notes.txt` file, or a message if there are no notes yet.

### Prompts

- **note_summary_prompt()**: Generates a prompt asking the AI to summarize all current notes in `notes.txt`.

## Technical Details

- All notes are stored in a plain text file named `notes.txt` in the project root. This file is created automatically if it does not exist.
- The server uses the [Model Context Protocol](https://modelcontextprotocol.io/) SDK and the `mcp[cli]` dependency.

### Windows Binary Mode Fix

If you use stdio transport on Windows, you may need to set binary mode for stdin/stdout. See the [MCP documentation](https://modelcontextprotocol.io/) for details.

## Troubleshooting

- Verify that all required packages are installed (`pip list` to check)
- Check that the absolute path in the configuration file is correct
- Make sure the MCP server is running with the proper version of Python (3.11)
- If you encounter issues, try running the MCP server directly to see any error output

## License

[MIT License](LICENSE)

## Acknowledgements

- This project uses the [Model Context Protocol](https://modelcontextprotocol.io/) SDK
