
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
# Make it so that when the user inputs addtodo, if the todo/thing is already there just update the quantity instead of creating a new one.
# Make like a back/reverse input. E.g. when you accidentally input addplace but you wanted to input display, you should be able to input in something so it goes back to asking you on what to do.
# Add a back input when you put ask then its goes to where are you going because it keeps on asking where are you going if the place isn't listed.
# Make it ask if you want to display the current list, add a new place, add new things to buy/do list, ask for the place to display your to do.
# Empty the dictionary later on, the key-value pairs are just there for testing purposes.
# Add a way to delete items and/or places.
# Add a way to dlete or "check off" items that have been done. 

# Remove add place, keep "add new place and new things (You can set it to None or something if you don't need to add anything to that new place)", and make a new "add existing things to existing place (put an try except that outputs "Place doesn't exist" if the place isn't listed)".
# Add message confirmations after doing a function.
# What happens the user wants to input more than one todo's? (Think of a way)
# You can't add more than one value to a key in a dictionary, find a way to make the user add multiple values to one key.
# I think dictionary displays values in alphabetical order, no matter the time/precedence you added it to the dictionary. Find a way to disable this and display it in order from oldest to the most recently added.
# When inputting in the "What do you want to do?", make it display something if the user didn't input the keywords available/displayed. 

import pprint
dict_places_do = {"Mcdonalds": "2 Coke Floats (Large)", "Mercury Drug": "4 tablets of Paracetamol"} 

# Main menu function that asks what you want to do
def main_menu(main_menu_input):
    if main_menu_input == "exit":
        pass    
    elif main_menu_input == "display":
        print("")
        pprint.pprint(dict_places_do)
    elif main_menu_input == "addexisting":
        addexisting_place = input("What is the name of the place you're adding to?: ")
        if addexisting_place not in dict_places_do:
            print("That place isn't listed.")
        else:
            addexisting_todo = input("What are you adding?: ")
            dict_places_do[addexisting_place] = addexisting_todo
            print("Successfully added")
    elif main_menu_input == "addtodo":
        addthings_place = input("What is the name of the place you're adding new todos?: ")
        addthings_todo = input("What is the new todo you want to add (you can choose to add nothing)?: ") # You can choose to remove the text inside the parantheses if you want.
        dict_places_do[addthings_place] = addthings_todo  
        print("Succesfully created and added.")
    elif main_menu_input == "ask":
        pass
    return main_menu_input

while True:     
    main_menu_return = main_menu(input("\nWhat do you want to do? (display, addtodo, addexisting, or ask) (or \"exit\" to exit): "))
    if main_menu_return == "exit" or main_menu_return == "ask":
        break

# Asks for the place you're going. (Make this a function)
while True:
    if main_menu_return == "exit":
        break
    while True:
        answer = input("Where are you going? (input \"exit\" to exit.): ")
        if answer == "exit":
            break
        elif answer in dict_places_do:
            print("\nHere's what you need to do there:\n " + dict_places_do[answer] + "\n")
        else:
            print("That place isn't listed.")
    break
    
