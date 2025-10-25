import os
import json 
import random
#so I dont have to type it out all the time... 
def invalid_input(): 
    print('Invalid input! Please try again.\n')

with open('QA/questions.json', 'r') as file:
    data = json.load(file)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_all_questions(data):
    all_questions = []
    for category in data["categories"]:
        all_questions.extend(data["categories"][category])
    return all_questions

#Enumerate gives an index-number (0,1,2..) and the value (eg. 'Rice')

def menu_choice(): #returns the questions
    while True:
        select = input('[1] Play random\n[2] Select category\n> ')
        if select == '1':
            questions = get_all_questions()
            return questions
        elif select == '2':
            chosen_category = select_category(data)
            questions = data["categories"][chosen_category]
            return questions
        else:
            invalid_input()

def select_category(data):
    clear_screen
    category_names = list(data["categories"].keys())

    for i, category in enumerate(data["categories"], start=1):
        print(f"{i}. {category}")

    selection = input("Select a category: \n")
    while True:
        if selection.isdigit() and 1 <= int(selection) <= len(category_names):
            chosen_category = category_names[int(selection)-1] #-1 to get the index which starts at 0
            return chosen_category
        else:
            invalid_input()


def ask_question(question_dict):
    clear_screen
    question = question_dict["question"]
    print(f'{question}')
    answers = []
    answers.extend(question_dict['decoys'])
    answers.append(question_dict['correct'])
    
    #shuffles answers and adds them to dict
    random.shuffle(answers)
    answer_mapping = {}
    for i, answer in enumerate(answers):
        letter = chr(65 + i)
        print(f'[{letter}] {answer}')
        answer_mapping[letter] = answer  # This adds the key-value pair

    #compare inoput
    while True:
        selection = input("Answer:\n> ").upper()
        if selection in answer_mapping:
            break
        else:
            invalid_input()
    
    #check if correct
    if answer_mapping[selection] == question_dict['correct']:
        print(f'Correct! {selection} was the right answer')
        return True
    else:
        print(f'False. [{question_dict["correct"]}] would have been the right answer!')
        return False
    

def exit():
    return False #Placeholder 

while exit() is False:
    print('## Welcome to Q&A ##\n')
    print()
    menu_choice