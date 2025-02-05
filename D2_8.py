#give a code for the output as *
#                             ***
#                            *****                 (You can generate a pyramid pattern based on user input in Python like this:)
#like this user input in python

n = int(input("Enter the number of rows: "))
# Generate the pyramid pattern
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

