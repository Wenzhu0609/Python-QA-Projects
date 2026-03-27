values = [5, 6.4, "Perfect"]
print(values[0])
print(values[1])
print(values[2])
print(values[-1]) # This is used to access the last element of the list
print(values[1:3]) # This will print the elements from index 1 to index 2 (3-1)
values.insert(2, "John") # This will insert "Rahul" at index 2 and shift the rest of the elements to the right
print(values)
print(values[2]) # This will print "Rahul"
values.append("Reese") # This will add "End" at the end of the list
print(values)
print(values[4]) # This will print "End"
del values[1] # This will delete the element at index 1 (6.4)
print(values)