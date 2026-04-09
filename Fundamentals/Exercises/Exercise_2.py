age = 25
height = 5.9
favorite_color = "blue"

print("Age: ", age, "Type: ", type(age))
print("Height: ", height, "Type: ", type(height))
print("Favorite Color: ", favorite_color, "Type: ", type(favorite_color))


user_data = {
    "Age": 25,
    "Height": 5.9,
    "Favorite Color": "blue"
}
for key, value in user_data.items():
    print(f"{key}: {value} | Type: {type(value)}")

