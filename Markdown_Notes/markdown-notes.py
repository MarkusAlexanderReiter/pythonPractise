import os
import json
from pathlib import Path

notes_dir = Path(__file__).parent/"notes"

#returns default directory and creates it if needed
def get_notes_directory(): 
    if not notes_dir.exists():
        notes_dir.mkdir()
        return notes_dir
    
