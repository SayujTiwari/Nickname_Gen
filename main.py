import random

#possible nicknames
nicknames = ["The Crusher", "The Scientist", "Twinkle-toes", "The Coder", "The Jester", "The Sloth", "Quick-Silver"]

# function to generate a random nickname
def get_random_nickname(first_name, last_name):
    return f"{first_name} \"{random.choice(nicknames)}\" {last_name}"

# function to display all nicknames
def display_all_nicknames(first_name, last_name):
    for nickname in nicknames:
        print(f"{first_name} \"{nickname}\" {last_name}")

# function to add a nickname
def add_nickname():
    nickname = input("Please enter a nickname to add: ")
    if nickname in nicknames:
        print(f"{nickname} is already in the nickname list.")
    else:
        nicknames.append(nickname)
        print(f"{nickname} added to the nickname list.")

# function to remove a nickname
def remove_nickname():
    nickname = input("Please enter a nickname to remove: ")
    if nickname in nicknames:
        nicknames.remove(nickname)
        print(f"{nickname} removed from the nickname list.")
    else:
        print(f"{nickname} was not found in the nickname list.")

# initial input for first and last name
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# main menu loop
while True:
    print(f"\nMAIN MENU ({first_name} {last_name})")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")

    choice = input("Please select an option: ")

    if choice == "1":
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        print(f"Current name is {first_name} {last_name}.")
    elif choice == "2":
        print("RANDOM NICKNAME")
        print(get_random_nickname(first_name, last_name))
    elif choice == "3":
        print("ALL NICKNAMES")
        display_all_nicknames(first_name, last_name)
    elif choice == "4":
        add_nickname()
    elif choice == "5":
        remove_nickname()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



