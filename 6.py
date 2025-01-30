# write a program to swap two given variables 
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Swapping the values using a temporary variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
