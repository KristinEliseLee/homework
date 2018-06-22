
def print_day(day, file): # day is the number of that day i.e. 3, 12, etc.

    print("Day{}".format(day))
    the_file = open(file)

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))

    the_file.close()


print_day(1, "um-deliveries-20140519.txt")
print_day(2, "um-deliveries-20140520.txt")
print_day(3, "um-deliveries-20140521.txt")
