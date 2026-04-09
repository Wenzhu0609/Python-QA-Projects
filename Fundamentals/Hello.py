# %%
print("Hello, my Python world!")
# This is my python program review.

a, b, c = 5, 6.4, "Perfect"
print(a, b, c)


#Compare a few ways to print the value of a variable:
#print("Value is" + b +"abcd")  
    #How it's written in other languages like Java, C#, etc. 
    #This will cause an error in python because b is a float and cannot be concatenated with a string directly.
#all phyton 3, we can use the format method to print variables:
print("{} {}".format("Value is", b))
#Python 3.6 and above, recommended way to print variables using f-strings:
print(f"Value is {10}")
#how to know the data type of a variable:
print(type(a))
print(type(c))
print(type("Value is"))
print(type(f"Value is {10}"))

