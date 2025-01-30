# find the odd or even without using ifelse(use list) 
n = list(range(1, 1000))  
n = int(input("enter a number:"))
result = ["Even","Odd"]   # [] is denotes a list
print(result[n % 2])