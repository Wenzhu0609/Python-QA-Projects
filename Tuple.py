values = (5, 6.4, "Perfect")
print(values[0])
print(values[1])
print(values[2])
print(values[-1]) # This is used to access the last element of the tuple
print(values[1:3]) # This will print the elements from index 1 to index 2 (3-1)
# values.insert(2, "John") # This will give an error because tuples are immutable
#print(values)
values[2] = "John" # This will also give an error because tuples are immutable
print(values)