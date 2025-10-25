import os

# Initialize the three poles
# If we have 3 disks, what should pole_a start as?
pole_a = [3, 2, 1]
pole_b = []
pole_c = []

poles = [pole_a, pole_b, pole_c]
num_disks = len(pole_a)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def display_poles(poles):
    max_height = max(len(pole) for pole in poles)
    for row in range (max_height):
        height_from_bottom = max_height - row - 1
        
        for pole in poles:
            if height_from_bottom < len(pole):
                print(f"{pole[height_from_bottom]}", end="    ")

            else: 
                print("[]", end="     ")
        print()
    for i in range(len(poles)):
        letter = chr(ord('A') + i)
        print(letter, end="     ")
    print()

def choose_pole(poles):
    valid_letters = [chr(ord('A') + i) for i in range(len(poles))]

    while True:
        choice = input("Select a pole: ").upper()
        if choice in valid_letters:
            index = ord(choice) - ord("A")
            return poles[index]
        
        else:
            print("[!] Invalid input, please try again.")

def take_disk(pole):
    if pole:
        disk = pole.pop()
        return disk
    else: 
        clear_screen()
        print("[!] Pole has no disks to move.")

def append_disk(pole,disk):
    if pole:
        top_disk = pole[-1]
        if disk > top_disk:
                print("[!] You may only place smaller disks on top of bigger disks!")
                return False
        else: 
            pole.append(disk) 
            return True
    else: 
        pole.append(disk)
        return True

def victory_check():
    if len(pole_c) == num_disks:
        return True
    else: return False


# Game loop
clear_screen()
print("###  Welcome to Hanoi! ###")
while victory_check() == False:
        display_poles(poles)
        print("Choose a pole whos disk you want to move.")
        take_pole = choose_pole(poles)
        disk = take_disk(take_pole)
        if disk:
            clear_screen()
            display_poles(poles)
            print(f"Where do you want to put Disk[{disk}]?")
            append_pole = choose_pole(poles)
            append_check = append_disk(append_pole, disk)
            if append_check == False:
                take_pole.append(disk)
                print(f"Disk[{disk}] has been returned.") 
            elif append_check == True:
                clear_screen()
clear_screen
display_poles
print("### Congratulations, you won!! ###")
