my_dict = { "name": "Alice", "age": 25, "profession": "Engineer"}

print(my_dict["name"])

print(my_dict.get("profession"))

for key, value in my_dict.items():
   print(f"{key}: {value}")
