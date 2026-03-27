#If else conditon
greeting = "Good Morning"
if greeting == "Good Morning":
    print("Condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")
# %%
greetings = input("Please enter your greeting: ")
if greetings == "Good Morning":
    print("Condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

umbrella = input("Is it raining outside? (yes/no): ")
if umbrella == "yes":
    print("Don't forget to bring your umbrella!")
else:
    print("Have a bright day!")



#for loop
obj = [2, 3, 5, 7, 9]
for i in obj:
    print("the value of i is: ")
    print(i)
    print("the value of i times 2 is: ")
    print(i*2)

list1 = [1, 2, 3, 4, 5 ]
for l in list1:
    print(f"the value of l is: {l}")
    print(f"the value of twice of l is: {l*2}")
# %%
# sum of First Natural numbers 1+2+3+4+5 = 15
summation = 0
for r in range(1, 6): # range(i,j) -> i to j-1
    summation = summation + r
    print(summation) # This will print the summation at each step of the loop
print(summation) # This will print the final summation after the loop is completed





# %%
