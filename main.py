# server.py
from mcp.server.fastmcp import FastMCP
import os
# Create an MCP server
mcp = FastMCP("AI Assistant Notes", dependencies=["mcp[cli]"])

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file_exists():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(note: str)-> str:
    """Add a note to the notes file
    
    Args:
        note: The note to add
        
    Returns:
        A message indicating that the note was saved
    """
    
    ensure_file_exists()
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    return "Note saved!"


@mcp.resource("notes://latest")
def get_latest_notes()-> str:
    """Get the latest notes from the notes file
    
    Returns:
        A string containing the latest notes
    """
    ensure_file_exists()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1:].strip() if lines else "No notes yet"


@mcp.prompt()
def note_summary_prompt()-> str:
    """
    Generate a prompt asking the AI to summarize all current notes.
    
    Returns:
        A string containing the summary of the notes
    """
    ensure_file_exists()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "No notes yet"

    # Summarize the notes
    prompt = f"Summarize the following notes:\n{content}"
    return prompt



