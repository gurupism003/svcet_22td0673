#WRITE A CODE TO IDENTIFY THE ONLY UNIQUE NUMBER FROM LIST OF PAIRS -  [1,1,2,2,3,3,4,5,5,]EG
def find_unique_number(nums):
    unique_num = 0
    for num in nums:
        unique_num ^= num
    return unique_num
nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5]
print(f"The unique number is: {find_unique_number(nums)}")
