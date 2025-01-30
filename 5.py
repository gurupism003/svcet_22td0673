# write a program to print the sum of the integers upto the given no5
n = int(input("Enter a number: "))

# Calculate the sum of integers from 1 to n
sum_of_numbers = sum(range(1, n+1))
print(f"The sum of integers up to {n} is: {sum_of_numbers}")
