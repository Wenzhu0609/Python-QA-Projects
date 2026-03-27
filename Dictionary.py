dic = {1:"first name", 2:"last name", "age":35}
print(dic[1])  # first name
print(dic[2])  # last name
print(dic["age"])  # 35. If the key is a string, it must be enclosed in quotes when accessing the value. If the key is an integer, it can be accessed without quotes.
print(dic.get(1))  # first name, successful search
print(dic.get("age"))  # 35, successful search
print(dic.get(3))  # None, unsuccessful search, but does not give an error or crash like dic[3] would
print(dic.get(3, "Not Found"))  # Not Found, unsuccessful search, but customizable and returns "Not Found" instead of None
dic[2] = "Maiden name"  # Updating the value of key 2
print(dic[2])  # Maiden name
del dic[1]  # Deleting the key-value pair with key 1
print(dic)  # {2: 'Maiden name', 'age': 35}
dic["city"] = "Toronto"  # Adding a new key-value pair to the dictionary
print(dic)  # {2: 'Maiden name', 'age': 35, 'city': 'Toronto'}
dic.update({1: "first name", 4: "email"})  # Adding multiple key-value pairs to the dictionary using the update method
print(dic)  # {2: 'Maiden name', 'age': 35, 'city': 'Toronto', 1: 'first name', 4: 'email'}
del dic["age"]  # Deleting the key-value pair with key "age"
del dic["city"]  # Deleting the key-value pair with key "city"
dic[3] = "age"  # Adding a new key-value pair to the dictionary
print(dic)  # {2: 'Maiden name', 1: 'first name', 4: 'email', 3: 'age'}
sorted_dic = dict(sorted(dic.items()))  # Sorting the dictionary by keys and creating a new sorted dictionary
print(sorted_dic)  # {1: 'first name', 2: 'Maiden name', 3: 'age', 4: 'email'}    

dic.clear()  # Clearing all key-value pairs from the dictionary
print(dic)  # {}

