#If else conditon
greeting = "Good Morning"
if greeting == "Good Morning":
    print("Condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

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


# sum of First Natural numbers 1+2+3+4+5 = 15
summation = 0
for r in range(1, 6): # range(i,j) -> i to j-1
    summation = summation + r
    print(summation) # This will print the summation at each step of the loop
print(f"final summation is {summation}") # This will print the final summation after the loop is completed

print("*****************************")

for k in range(1,10,2):
    print(k)

print("**************Skipping first index***************")

for m in range(10):
    print(m)


# While Loop
it = 4
while it > 1:
    print(it)
    it = it - 1
print("While loop is completed.")

it = 4
while it > 1:
    if it != 3:     #this is to hide the data that you know you don't want to display, but the whole loop was still executed.
        print(it)
    it = it - 1
print("While loop is completed.")

it = 4
while it > 1:
    if it == 3:
        break       # this is to stop the loop abruptly once it reaches the targeted data. Application: once we find the target data, we'll stop searching and move on.
    print(it)
    it = it - 1
print("While loop is completed.")

it = 10
while it > 1:
    if it == 9:
        continue    # satisfying this condition will skip everything afterwards and restart in the new iteration, meaning it woun't do the calculation of it = it - 1, therefore will always start with it = 9 and stay in the loop although nothing's being printed.
    if it == 3:
        break
    print(it)
    it = it - 1
print("While loop is completed.")   # This statement will never get printed since the while loop never finishes.
# %%
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue    # satisfying this condition will skip everything afterwards and restart in the new iteration, but since we added it = it - 1 before "continue", we are starting the new iteration with new it = 8 instead of 9, and 9 does not get printed. Application: to skip heavy logics if certain criteria's not met, e.g. skip an empty row to move on to the next line.
    if it == 3:
        break
    print(it)
    it = it - 1
print("While loop is completed.")