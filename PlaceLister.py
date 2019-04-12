
# Program asks for a list and displays the things you need to do there.

# Make comment per each piece of code

# TO DO:
# 1. Make it ask if you want to display the list.
# 2. Make the output pp.ppformat style and equal indentation/column width.
# 3. In the dictionary display an ordered number that numbers the items in each place so later the user can just put the number with the todo thing in an input that asks for the number to delete that thing off the place list.
# Use setdefault() so when you ask the person if he wants to addplace and puts an existing place it will overwite that place and not create a new place instead.
# Remove brackets when printing dictionary.
# Make the code into functions to make it cleaner?
# Make it so you can delete todos/things.
# Make it so that you can enter multiple input and like maybe you can tell the user to seperate it with something so that the program reads each seperator as a stop and interprets the next string as a new todo.
# Make it so that when the user inputs addthings, if the todo/thing is already there just update the quantity instead of creating a new one.
# Make like a back/reverse input. E.g. when you accidentally input addplace but you wanted to input display, you should be able to input in something so it goes back to asking you on what to do.
# Make a repository and try out git/GitHub commands and decide on the repository license.

import pprint

dict_places_do = {
    "Mcdonalds": "2 Coke Floats (Large)", "Mercury Drug": "4 tablets of Paracetamol"}

while True:
    answer_decide = input(
        "What do you want to do? (display, addplace, addthings, or ask) (or exit to exit): ")
    if answer_decide == "exit":
        break
        # Make this line as a code to make the whole program exit if the input is "exit".
    elif answer_decide == "display":
        pprint.pprint(dict_places_do)
    elif answer_decide == "addplace":
        add_place = input("What is the name of the place?: ")
        dict_places_do[add_place] = None
    elif answer_decide == "addthings":
        add_things1 = input(
            "What is the name of the place you're adding new todos?: ")
        add_things2 = input("What is the new todo you want to add?: ")
        dict_places_do[add_things1] = add_things2


# Asks for the place you're going.
while True:
    answer = input("Where are you going? (input \"exit\" to exit.): ")
    if answer == "exit":
        break
    elif answer in dict_places_do:
        print("Here's what you need to do there: " + dict_places_do[answer])
    else:
        print("That place isn't listed.")

# Make it ask if you want to display the current list, add a new place, add new things to buy/do list, ask for the place to display your to do.
