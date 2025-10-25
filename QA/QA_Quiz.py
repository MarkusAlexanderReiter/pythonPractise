import os
import json 
import random

with open('QA/questions.json', 'r') as file:
    data = json.load(file)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

letters = ['A', 'B', 'C','D']
options = {}


def get_all_questions(data):
    all_questions = []
    for category in data["categories"]:
        all_questions.extend(data["categories"][category])
    return all_questions

#Enumerate gives an index-number (0,1,2..) and the value (eg. 'Rice')

def menu_choice():
    while True:
        select = input('[1] Play random\n[2] Select category\n> ')
        if select == '1':
            print('1')
            return select
        elif select == '2':
            select_category
            break
        else:
            print('Invalid input! Please try again.\n')

def select_category()

def exit():
    return False #Placeholder 

while exit() is False:
    print('## Welcome to Q&A ##\n')
    print()
    menu_choice