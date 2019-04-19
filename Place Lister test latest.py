
# Program asks for a list and displays the things you need to do there.

# Make comment per each piece of code

# TO DO:
# 2. Make the output equal indentation/column width.
# 3. In the dictionary display an ordered number that numbers the items in each place so later the user can just put the number with the todo thing in an input that asks for the number to delete that thing off the place list.
# Remove brackets when printing dictionary.
# Make the code into functions to make it cleaner?
# Make it so you can delete todos/things. ###################### 1. Delete an existing place. 2. Delete existing todos.
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
# I think dictionary displays values in alphabetical order, no matter the time/precedence you added it to the dictionary. Find a way to disable this and display it in order from oldest to the most recently added.
# When inputting in the "What do you want to do?", make it display something if the user didn't input the keywords available/displayed. 

# Current: You can't add more than one value to a key in a dictionary, find a way to make the user add multiple values to one key.
# Left off - Line 54: When addtodo a new a place, since you make it equal to [], it clears the previous todos in it. Find a way brah!
# When you choose addtodo option, you should be able to have the choice to exit if you don't wan tot add a new one or existing.
# Make it so you can delete of the list.

import pprint

dict_main = {"Mcdonalds": ["2 Coke Floats (Large)", "5 Large Fries", "10 Chocolate Sundaes", "Ketchup", "7 Cheeseburgers"], "Mercury Drug": ["4 tablets of Paracetamol"]} #

# Main menu function that asks what you want to do
def main_menu(main_menu_input):
    if main_menu_input == "exit": # If input is "exit"
        pass    
    elif main_menu_input == "display":  # If input is "display"
        print("")
        pprint.pprint(dict_main)   
    elif main_menu_input == "addexisting": # If input is "addexisting"
        addexisting_place = input("What is the name of the place you're adding to?: ")
        if addexisting_place not in dict_main: 
            print("That place isn't listed.")
        else:
            addexisting_todo = input("What are you adding?: ")  
            dict_main[addexisting_place].append(addexisting_todo) 
            print("Successfully added")
    elif main_menu_input == "addtodo": # If input is "addtodo"
        addthings_place = input("What is the name of the place you're adding new todos?: ")
        addthings_todo = input("What is the new todo you want to add (you can choose to add nothing by entering nothing)?: ") 
        if addthings_place in dict_main:
            dict_main[addthings_place].append(addthings_todo)
        else:
            dict_main[addthings_place] = []
            dict_main[addthings_place].append(addthings_todo)  
        print("Succesfully created and added.")
    elif main_menu_input == "ask": # If input is "ask"
        pass
    elif main_menu_input = "del": # If input is "del"
        del_answer = input("What do you want to del (place or todo)?: ")
        if del_answer == "place":
            del_place = input("What is the name of the place (this will remove all existing lists associated with that place)?: ")
            if del_place in dict_main:
                dict_main.pop(delplace)
            print("Succesfully deleted.") # You can change this later, it's your choice if you want the program to say that the place doesn't exist.
        elif del_answer == "todo":
            while True:
                del_place2 = input("What is the name of the place?: ")
                if del_place2 in dict_main:
                    print("These is the place and the todos associated with it:\n")
                    pprint.pprint(dict_main[delplaces2])
                    print("")
                    del_todo = input("What is the todo you want to delete?") # Can you make the list items have a number at the beginning so you can easily pick the number that you want to delete instead of picking out the whole phrase?
                    dict_main[del_place2].remove(del_todo) # Check this del_answer == "todo" and put if and else stating that if it's in the main dictionary, say if it is or not avaiable then go back to the loop or break if it is available and printout "Success!"

        
        elif == "exit":

        else:
            print("That place doesn't exist!")

    return main_menu_input

while True:     
    main_menu_return = main_menu(input("\nWhat do you want to do? (display, addtodo, addexisting, del, or ask) (or \"exit\" to exit): "))
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
        elif answer in dict_main:   
            print("\nHere's what you need to do there:\n")
            pprint.pprint(dict_main[answer])
            print("")
        else:
            print("That place isn't listed.")
    break

