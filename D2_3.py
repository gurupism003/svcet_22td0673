#output as  ***               (for the input of 3)
#           * *
#           ***
n = int(input("Enter the number of rows: "))      #  no of rows of square or size of square
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
           print("*", end="")
        else :
           print(" ", end="")
    print()
