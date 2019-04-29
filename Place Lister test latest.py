# Project Idea: make some kind of game like an rpg! Add a thing on the game like if the program asks you something and you reply make the program wait using the printing command while printing out .... (periods to make the user think the program is thinking/takinghis time.)


# Program asks for a list and displays the things you need to do there.

# Make comment per each piece of code

# TO DO:
# 2. Make the output equal indentation/column width.
# 3. In the dictionary display an ordered number that numbers the items in each place so later the user can just put the number with the todo thing in an input that asks for the number to delete that thing off the place list.
# Remove brackets when printing dictionary.
# Make the code into functions to make it cleaner?
# Make it so that you can enter multiple input and like maybe you can tell the user to seperate it with something so that the program reads each seperator as a stop and interprets the next string as a new todo.
# Make it so that when the user inputs addtodo, if the todo/thing is already there just update the quantity instead of creating a new one.
# Make like a back/reverse input. E.g. when you accidentally input addplace but you wanted to input display, you should be able to input in something so it goes back to asking you on what to do.
# Add a back input when you put ask then its goes to where are you going because it keeps on asking where are you going if the place isn't listed.
# Empty the dictionary later on, the key-value pairs are just there for testing purposes.
# Add a way to delete items and/or places.
# Make the list pretties when user calls displayinput choice and arrange it by alphabetical order. 

# Remove add place, keep "add new place and new things (You can set it to None or something if you don't need to add anything to that new place)", and make a new "add existing things to existing place (put an try except that outputs "Place doesn't exist" if the place isn't listed)".
# Add message confirmations after doing a function.
# What happens the user wants to input more than one todo's? (Think of a way)
# I think dictionary displays values in alphabetical order, no matter the time/precedence you added it to the dictionary. Find a way to disable this and display it in order from oldest to the most recently added.
# When inputting in the "What do you want to do?", make it display something if the user didn't input the keywords available/displayed. 

# When you choose addtodo option, you should be able to have the choice to exit if you don't wan tot add a new one or existing. ####


# Make an option to display the current places or lists if they want/put an input when deleting places and/or todos so they can see what exists if they forget the things they want to delete.
#Find a way to save list because it discards the list after the program terminates.
# Maybe add a lower on all inputs so it's not so sensitive to cases? (Response: I'll think about it.)
# Make code pretty
# Make a website or some gui that runs this code maybe?
# Find out what is the different between addexisting and addtodo. If it's the same it's redundant, so delete one.
# Make like dividers like lines like this in top and the bottom of the command in out put using --------- or ********* for design!
#Make an input that makes the user edit the names of the places like change BurgerKing to Burger King.
# Make the program output out somethinglike ("That place already exists, I just updated it witt he new todos") when using the todo input choice.
# Make the program output something if the choice isn't a parameter (or in some cases output something if it's a paramter to indicate that the command was succesful).
# Find out new names for the input choices xD!


import pprint

dict_main = {"Mcdonalds": ["2 Coke Floats (Large)", "5 Large Fries", "10 Chocolate Sundaes", "Ketchup", "7 Cheeseburgers"], "Mercury Drug": ["4 tablets of Paracetamol"]}

# Main menu function that asks what you want to do
def main_menu(main_menu_input):
    if main_menu_input == "exit": 
        return main_menu_input    

    elif main_menu_input == "display":  
        print("")
        pprint.pprint(dict_main)

    elif main_menu_input == "addexisting": 
        addexisting_place = input("What is the name of the place you're adding to?: ")
        if addexisting_place not in dict_main: 
            print("That place isn't listed.")
        else:
            addexisting_todo = input("What todo are you adding?: ")  
            dict_main[addexisting_place].append(addexisting_todo) 
            print("Successfully added")

    elif main_menu_input == "newplaceandtodo": 
        addthings_place = input("What is the name of the new place you're creating?: ")
        addthings_todo = input("What is the new todo you want to add (you can choose to add nothing by entering nothing)?: ")
        if addthings_place != "":
            if addthings_place in dict_main:
                if addthings_todo != "":
                    dict_main[addthings_place].append(addthings_todo)
            else:
                dict_main[addthings_place] = []    
            print("Successfully created and added.")
        else:
            print("You didn't enter a name.")

        # if addthings_todo == "":
        # else:
        #     dict_main[addthings_place].append(addthings_todo)
        #     print("Succesfully created and added.")

    elif main_menu_input == "del": 
        del_answer = input("What do you want to del (place or todo)?: ")
        if del_answer == "place":
            print("Places in list:")
            for key in dict_main.keys():
                print(key)        
            del_place = input("\nWhat is the name of the place (this will remove all existing lists associated with that place)?: ")
            if del_place in dict_main:
                dict_main.pop(del_place)
                print("Succesfully deleted.") 
            else:
                print("That place doesn't exist.")
        elif del_answer == "todo":
            while True:
                del_place2 = input("What is the name of the place?: ")
                if del_place2 in dict_main:
                    print("These is the place and the todos associated with it:\n")
                    pprint.pprint(dict_main[del_place2])
                    print("")
                    del_todo = input("What is the todo you want to delete?: ") # Can you make the list items have a number at the beginning so you can easily pick the number that you want to delete instead of picking out the whole phrase? My response: I think  you can do this by making something like sublists but the main list is numbers and put the list message as a sublist of that main list number e.g. [1]["Buy 2 Fries"], [2]["Buy 5 Burgers"]
                    if del_todo in dict_main[del_place2]:
                        dict_main[del_place2].remove(del_todo)
                        print("Success!")
                    else:
                        print("That todo doesn't exist.")
                else:
                    print("That place doesn't exist.")
                break

    elif main_menu_input == "ask":
        answer = input("Where are you going?: ")
        if answer in dict_main:
            print("\nHere's what you need to do there:\n")
            pprint.pprint(dict_main[answer])
            print("")
        else:
            print("That place isn't listed.")


# The main question. It asks for the main inputs.
while True:     
    main_menu_return = main_menu(input("\nWhat do you want to do? (display, newplaceandtodo, addexisting, del, ask, or exit): "))
    if main_menu_return == "exit":
        break