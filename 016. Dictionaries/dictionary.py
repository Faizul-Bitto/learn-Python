userDictionary = {"userName": "JohnDoe", "name": "John", "age": 32}
print(userDictionary)
print(userDictionary.get("userName"))

userDictionary["married"] = True
print(userDictionary)
print(len(userDictionary))

userDictionary.pop("name")
print(userDictionary)

for x, y in userDictionary.items():
    print(x, y)

print(userDictionary.items())

userDictionary2 = userDictionary.copy()
userDictionary2.pop("age")
print(userDictionary2)

userDictionary.clear()
print(userDictionary)
