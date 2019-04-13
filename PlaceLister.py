
# Program asks for a list and displays the things you need to do there.

# Make comment per each piece of code

# TO DO:
# 2. Make the output equal indentation/column width.
# 3. In the dictionary display an ordered number that numbers the items in each place so later the user can just put the number with the todo thing in an input that asks for the number to delete that thing off the place list.
# Use setdefault() so when you ask the person if he wants to addplace and puts an existing place it will overwite that place and not create a new place instead.
# Remove brackets when printing dictionary.
# Make the code into functions to make it cleaner?
# Make it so you can delete todos/things.
# Make it so that you can enter multiple input and like maybe you can tell the user to seperate it with something so that the program reads each seperator as a stop and interprets the next string as a new todo.
# Make it so that when the user inputs addthings, if the todo/thing is already there just update the quantity instead of creating a new one.
# Make like a back/reverse input. E.g. when you accidentally input addplace but you wanted to input display, you should be able to input in something so it goes back to asking you on what to do.
# Add a back input when you put ask then its goes to where are you going because it keeps on asking where are you going if the place isn't listed.
# Make it ask if you want to display the current list, add a new place, add new things to buy/do list, ask for the place to display your to do.
# Empty the dictionary later on, the key-value pairs are just there for testing purposes.


import pprint
dict_places_do = {"Mcdonalds": "2 Coke Floats (Large)", "Mercury Drug": "4 tablets of Paracetamol"} 

# Main menu function that asks what you want to do
def main_menu(main_menu_input):
    #main_menu_input = input("What do you want to do? (display, addplace, addthings, or ask) (or exit to exit): ")
    if main_menu_input == "exit":
        pass
    elif main_menu_input == "display":
        print("")
        pprint.pprint(dict_places_do)
    elif main_menu_input == "addplace":
        add_place = input("What is the name of the place?: ")
        dict_places_do[add_place] = None
    elif main_menu_input == "addthings":
        add_things_place = input("What is the name of the place you're adding new todos?: ")
        add_things_todo = input("What is the new todo you want to add?: ")
        dict_places_do[add_things_place] =add_things_todo
    elif main_menu_input == "ask":
        pass
    return main_menu_input

while True:     
    main_menu_return = main_menu(input("\nWhat do you want to do? (display, addplace, addthings, or ask) (or \"exit\" to exit): "))
    if main_menu_return == "exit" or main_menu_return == "ask":
        break

# Asks for the place you're going. (Make this a function)
while True:
    if main_menu_return == "exit":
        break
    else:
        answer = input("Where are you going? (input \"exit\" to exit.): ")
        if answer == "exit":
            break
        elif answer in dict_places_do:
            print("\nHere's what you need to do there:\n " + dict_places_do[answer] + "\n")
        else:
            print("That place isn't listed.")
