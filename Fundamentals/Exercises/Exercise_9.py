# Customized Greeting Based on Time of Day

user = 16
if 5 <= user <= 11:
    print("Good Morning")
elif 12 <= user <= 17:
    print("Good Afternoon")
elif 18 <= user <= 21:
    print("Good Evening")
else:
    print("Good Night")
print("Greeting code has completed.")



# %%
user = 19

def get_daytime(user):
    if 5 <= user <= 11:
        return "Good Morning"
    elif 12 <= user <= 17:
        return "Good Afternoon"
    elif 18 <= user <= 21:
        return "Good Evening"
    else:
        return "Good Night"

greeting = get_daytime(user)
print(greeting)
print("Greeting code has completed.")