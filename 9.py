#give a code for the output as *****
#                               ****
#                                ***
#                                 **
#                                  *             
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)
