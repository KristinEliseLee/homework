the_story_file = open("lee_adventure.txt")
the_story = list(the_story_file)
the_story_file.close()

# read_section prints all lines between the start and stop markers in the list.
def read_section(start, stop):
    i = 0
    while the_story[i] != start:
        i += 1
    i += 1
    while the_story[i] != stop:
        if "{}" in the_story[i]:
            print(the_story[i].format(name))
        else:
            print(the_story[i])
        i += 1

print("Hello!")

# This part gets the user to type in a name, or names them Bob
# if they don't type in anything or type in something that starts with a non-letter
name = input("What is your name? ")
tries = 1

while (len(name) == 0 or name[0].isalpha() == False) and tries < 3:
    name = input("I asked for your name. What is it? ")
    tries += 1

if len(name) == 0 or name[0].isalpha() == False:
    print ("I'm just gonna call you Bob.")
    name = "Bob"

end = 0   # This exists only for the while loop end condition.

while end == 0:
    read_section("- START -\n", "-Choice 1 - 1 -\n")

    choice1 = input("Type the number of your choice: ")

    if choice1 == "1":

        read_section("-Choice 1 - 1 -\n", "-Choice2 - 1 -\n")

        choice2 = input("Type the number of your choice: ")

        if choice2 == "1":
            read_section("-Choice2 - 1 -\n", "-Choice2 - 2 -\n")

        elif choice2 == "2":
            read_section("-Choice2 - 2 -\n", "-Choice1 - 1 cont. -\n")

        elif choice2 != "1" and choice2 != "2":
            print("For not being able to follow instructions, you were eaten by a grue.")
            end = 1
            break

        read_section("-Choice1 - 1 cont. -\n", "-Choice3 - 1 -\n")

        choice3 = input("Type the number of your choice: ")

        if choice3 == "1":
            read_section("-Choice3 - 1 -\n", "-Choice3 - 2 -\n")

        elif choice3 == "2":
            read_section("-Choice3 - 2 -\n", "-Choice1 - 2 -\n")

        elif choice3 != "1" and choice3 != "2":
            print("For not being able to follow instructions, you were eaten by a grue.")
            end = 1
            break
        end = 1
        break

    elif choice1 == "2":
        read_section("-Choice1 - 2 -\n", "-Choice4 - 2 -\n")

        choice4 = input("Type the number of your choice: ")
        if choice4 == "2":
            read_section("-Choice4 - 2 -\n", "-Choice4 - cont. -\n")

        elif choice4 != "1" and choice4 != "2":
            print("For not being able to follow instructions, you were eaten by a grue")
            end = 1
            break

        read_section("-Choice4 - cont. -\n", "-Choice4 - 2 cont. -\n")

        if choice4 == "2":
            read_section("-Choice4 - 2 cont. -\n", "-Choice4 - cont. -\n")

        read_section("-Choice4 - cont. -\n", "-END-\n")
        end = 1
        break

    elif choice1 != "1" and choice1 != "2":
        print("For not being able to follow instructions, you were eaten by a grue.")
        end = 1
        break
    end = 1
    break
