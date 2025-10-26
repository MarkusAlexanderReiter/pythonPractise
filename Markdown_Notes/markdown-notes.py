import os
import json
from pathlib import Path

notes_dir = Path(__file__).parent/"notes"

#shortcut functions...
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def invalid_input(): 
    print('Invalid input! Please try again.')

#returns default directory and creates it if needed
def get_notes_directory(): 
    if not notes_dir.exists():
        notes_dir.mkdir()
        return notes_dir
    
def menu():
    while True:
        clear_screen
        select = input('[1] Create new file\n[2] View/search\n[3] Settings\n[0] Exit\n\n> ')
        if select == '1':
            print('1')
        elif select == '2':
            print('2')
        elif select == '3':
            print('3')
        elif select == '4':
            break
        else: invalid_input()

    
    