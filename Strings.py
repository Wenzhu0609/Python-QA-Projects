str1 = "RahulShettyAcademy.com"
str2 = "Consulting Firm"
str3 = "RahulShetty"
str4 = "Great !"
str5 = " Great!      "

# To print substring in Python
print(str1[1])   # a
print(str1[0:5]) # Rahul
print(str1 + str2)  # concatenation

print(str3 in str1) # check if a substring exist in the main string; returs boolean results, either retrun true or false. Isage of "in" here in comparison to List, which checks if the entire item exist.
var1 = str1.split(".")  # Creats a list, defult uses space to split. The separator is not included in the list.
print(var1)
print(var1[0])

print(str4)
var2 = str4.strip()
print(var2)     # Doesn't trim spaces within the text
print(f"[{str5}]")
var3 = str5.strip()     # Trims the leading and trailing spaces
print(f"[{var3}]")     
var4 = str5.lstrip()    # Only trims the leading spaces
print(f"[{var4}]")
print(f"the length of this string is {len(var4)} characters")
var5 = str5.rstrip()    # Only trims the tailing spaces
print(f"[{var5}]")
print(f"the length of this string is {len(var5)} characters")
