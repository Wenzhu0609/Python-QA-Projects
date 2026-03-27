# For loop with numbers

# What I wrote:
list1 = [1, 4, 7, 10]       # Golden standard to name lists with a plural noun, good for readability and debugging
for i in list1:             # i is usually used as a variable name for index
    three_times_i = i * 3   # code with a self-documenting name, good for readability and debugging
    print(three_times_i)
    
# What instructor wrote:
numbers = [1, 4, 7, 10]
for num in numbers:         # num is usually used as a variable name for the elements in a list, shows what's inside the list, good for readability and debugging
    print(num * 3)          # simple one for all code, good for simple functions, but not good for readability and debugging when the code is more complex

# The "Pro" Hybrid Way by Gemini:
numbers = [1, 4, 7, 10]

for number in numbers:
    tripled_value = number * 3
    print(tripled_value)

# They all do the same thing, but the "Pro" way is more readable and easier to debug when the code is more complex. The variable names are more descriptive and self-documenting, which makes it easier to understand what the code is doing at a glance.