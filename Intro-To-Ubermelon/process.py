# Gets the data from um-server-01.txt
log_file = open("um-server-01.txt")

# Creates a function that:
def sales_reports(log_file):
    # cycles through the lines in the file
    for line in log_file:
        # removes the \n from the end of the string
        line = line.rstrip()
        # sets day equal to the first 3 characters of the string
        day = line[0:3]
        # if day says "Mon"
        if day == "Mon":
            # print the whole line
            print(line)

# runs the function on the file
sales_reports(log_file)
log_file.close()
