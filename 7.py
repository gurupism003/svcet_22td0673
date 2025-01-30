# rotate a list with k placement
set = [1, 2, 3, 4, 5, 6, 7]  
k = int(input("Enter the number of rotations: "))

# Rotate the list by k positions
rotated_list = set[-k % len(set):] + set[:-k % len(set)]
print("Rotated list:", rotated_list)