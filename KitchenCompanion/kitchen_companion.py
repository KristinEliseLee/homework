from random import randint

ingredients = open("/home/vagrant/src/homework/kitchen_companion.txt", "r")
ingredients_list = list(ingredients)
ingredients.close()

# The below for loop gets rid of the newline character at the end of each item
# in the list.

for i in range(len(ingredients_list)):
    old = ingredients_list[i]
    ingredients_list[i] = old[:len(old)-1]

def options():
    print("Type A to add an ingredient")
    print("Type R to remove an ingredient")
    print("Type L to list all ingredients alphabetically")
    print("Type Q to quit")
    print("Type RANDOM for a random ingredient")
    print("Type CHECK to see if you have all the ingredients you need")

print("Welcome to your Kitchen Companion!")
print()
options()

quit = 0       # This is only for the while loop condition.

while quit != 1:
    print()
    user_wants = input("What would you like to do? ").lower()

    if user_wants == "q":
        quit = 1
        break

    elif user_wants == "a":
        thing_to_add = input("What would you like to add? ").lower()

        if thing_to_add in ingredients_list:
            print("That's already in your list of ingredients.")

        else:
            ingredients_list.append(thing_to_add)
            print("You added {} to your list of ingredients.".format(thing_to_add))

    elif user_wants == "r":
        thing_to_remove = input("what would you like to remove? ").lower()

        if thing_to_remove in ingredients_list:
            ingredients_list.remove(thing_to_remove)
            print("You removed {} from your list of ingredients.".format(thing_to_remove))

        else:
            print("That's not in your list of ingredients.")

    elif user_wants == "l":
        if len(ingredients_list) == 0:
            print("You have no ingredients! You should add some.")
        else:
            print("Your list of ingredients is: ")
            ingredients_list.sort()
            for x in ingredients_list:
                print(x)

    elif user_wants == "random":
        total = len(ingredients_list) - 1
        rand = randint(0, total)
        print(ingredients_list[rand])

    elif user_wants == "check":
        things_needed = input("Type the list of ingredients your recipee needs, separated by commas: ")

        things_needed_list = things_needed.split(",")
        for i in range(len(things_needed_list)):
            things_needed_list[i] = things_needed_list[i].lower()

            # The below if statments are to get rid of any starting or trailing spaces.
            if things_needed_list[i][0] == " ":
                things_needed_list[i] = things_needed_list[i][1:]
            if things_needed_list[i][len(things_needed_list[i])-1] == " ":
                things_needed_list[i] = things_needed_list[i][:len(things_needed_list[i])-1]

        things_missing = []
        for i in things_needed_list:
            if i not in ingredients_list:
                things_missing.append(i)

        things_missing.sort()          # This is just to make it print neater.

        if len(things_missing) > 0:
            print("You're missing: {}".format(", ".join(things_missing)))

        else:
            print("You have all those ingredients!")

    else:
        print("\"{}\" is not a valid option. Your options are:".format(user_wants))
        options()

ingredients_list.sort()
ingredients = open("/home/vagrant/src/homework/kitchen_companion.txt", "w")

for i in ingredients_list:
    ingredients.write("{}\n".format(i))

ingredients.close

print("Thank you for using your Kitchen Companion!")
print("Goodbye.")
