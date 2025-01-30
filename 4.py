#create a list[1 to 100] and use for loop to print the numbers divisible by 2 and skip numbers divisibly by 100 in python
n = list(range(1, 101))  
for num in n:
    if num % 100 == 0:  # Skip numbers divisible by 100
        continue
    if num % 2 == 0:  # Print numbers divisible by 2
        print(num)