#hello 
#first create an empty list
my_list = []
#print the list to see that it is empty
print(my_list)
# then append some items to it
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# Print the list to see the items
print(my_list)

#add a number to the 2nd position
my_list.insert(1, 15)
# Print the list to see the updated items
print(my_list)
# extend the list with another list
my_list.extend([50, 60, 70])
# Print the list to see the extended items
print(my_list)
# remove the last element from the list
my_list.pop()
# Print the list to see the items after popping
print(my_list)
# sort the list in ascending order
my_list.sort()
# Print the sorted list
print(my_list)
# Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")
