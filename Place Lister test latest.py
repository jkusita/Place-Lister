# Project Idea: make some kind of game like an rpg! Add a thing on the game like if the program asks you something and you reply make the program wait using the printing command while printing out .... (periods to make the user think the program is thinking/takinghis time.)

# Program asks for a list and displays the things you need to do there.

# Make comment per each piece of code

# TO DO:
# 3. In the dictionary display an ordered number that numbers the items in each place so later the user can just put the number with the todo thing in an input that asks for the number to delete that thing off the place list.
# Make the code into functions to make it cleaner?
# Make it so that you can enter multiple input and like maybe you can tell the user to seperate it with something so that the program reads each seperator as a stop and interprets the next string as a new todo.
# Make like a back/reverse input. E.g. when you accidentally input addplace but you wanted to input display, you should be able to input in something so it goes back to asking you on what to do.
# Add a back input when you put ask then its goes to where are you going because it keeps on asking where are you going if the place isn't listed.
# Empty the dictionary later on, the key-value pairs are just there for testing purposes.

# What happens the user wants to input more than one todo's? (Think of a way)
# I think dictionary displays values in alphabetical order, no matter the time/precedence you added it to the dictionary. Find a way to disable this and display it in order from oldest to the most recently added.. 
# When you choose addtodo option, you should be able to have the choice to exit if you don't wan tot add a new one or existing. ####


# Make an option to display the current places or lists if they want/put an input when deleting places and/or todos so they can see what exists if they forget the things they want to delete.
#Find a way to save list because it discards the list after the program terminates.
# Maybe add a lower on all inputs so it's not so sensitive to cases? (Response: I'll think about it.)
# Make code pretty
# Make a website or some gui that runs this code maybe?
# Find out what is the different between addexisting and addtodo. If it's the same it's redundant, so delete one.
#Make an input that makes the user edit the names of the places like change BurgerKing to Burger King.
# Make the program output out somethinglike ("That place already exists, I just updated it witt he new todos") when using the todo input choice.
# Make the program output something if the choice isn't a parameter (or in some cases output something if it's a paramter to indicate that the command was succesful).
# Find out new names for the input choices xD!
# Find out a way to not put that extra space between the list and the line in display.



import pprint

# Still implementing variables
longest_key = 0
longest_value = 0
display_seperator = 3
todo_longest_value = 0


dict_main = {"Mcdonalds": ["2 Coke Floats (Large)", "5 Large Fries", "10 Chocolate Sundaes", "Ketchup", "7 Cheeseburgers"], "Mercury Drug": ["4 tablets of Paracetamol"]}

# Main menu function that asks what you want to do
def main_menu(main_menu_input):
    global longest_key, longest_value
    if main_menu_input == "exit": 
        return main_menu_input    

    elif main_menu_input == "display":  
        print("")

        # Gets the length of the longest key and value/sublist(value) in the dictionary
        for j in dict_main.keys(): 
            if len(j) > longest_key:
                longest_key = len(j)
        for i in dict_main.keys():
            for c in dict_main[i]:
                if len(str(c)) > longest_value:
                    longest_value = len(str(c))
        
        # Prints out the heading and subheading.
        todo_longest_value = int((longest_value - len("[TODO]"))/2)
        print("PLACE-LISTER".center(longest_key + longest_value + display_seperator, '-'))
        print("[Places]".center(longest_key), end = "")
        print( "[TODO]".rjust(display_seperator + len("[TODO]") + todo_longest_value))

        # Prints out the keys and values from the dictionary.
        for a in dict_main.keys():
            print(a.ljust(longest_key), end = "")
            for b in dict_main[a]:
                if b == dict_main[a][0]:
                    print(str(b).rjust(len(str(b)) + display_seperator)) #
                else:
                    print(str(b).rjust(longest_key + len(str(b)) + display_seperator))
            print("")
        print("-" * (longest_key + longest_value + display_seperator))

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
        if addthings_place == "":
            print("You didn't enter a name.")
        else:
            addthings_todo = input("What is the new todo you want to add (you can choose to add nothing by entering nothing)?: ")
            if addthings_place != "":
                if addthings_place in dict_main:
                    if addthings_todo != "":
                        dict_main[addthings_place].append(addthings_todo)
                else:
                    dict_main[addthings_place] = [addthings_todo]    
                print("Successfully created and added.")

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
            for i in dict_main[answer]:
                print("• "+ i + "\n")
        else:
            print("That place isn't listed.")

    elif main_menu_input == "":
        print("Please enter something.")


# The main question. It asks for the main inputs.
while True:     
    main_menu_return = main_menu(input("\nWhat do you want to do? (display, newplaceandtodo, addexisting, del, ask, or exit): "))
    if main_menu_return == "exit":
        break
