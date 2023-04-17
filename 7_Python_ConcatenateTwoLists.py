#Python progrm to concatenate two list

#Method 1: Using + operator
l1 = [2,4,5,"ah","uh"]
l2 = [5,8,9,"Yes","no"]

l12 = l1 + l2

print(l12)

#Mehtod 2: With unique values using set
l1 = [2,4,5,"ah","uh"]
l2 = [5,8,9,"Yes","no"]

l12 = set(l1 + l2)

print(l12) # will print unique values from l1 and l2 in SET format

l12 = list(set(l1 + l2))

print(l12) # will print unique values from l1 and l2 in list format

#Method 3: Using extend function
l1 = [2,4,5,"ah","uh"]
l2 = [5,8,9,"Yes","no"]

l1.extend(l2)
print(l1) #prints without unique values
