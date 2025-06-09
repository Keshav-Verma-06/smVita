mydict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(mydict.get("name"))  # Output: John
print(mydict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(mydict.values())  # Output: dict_values(['John', 30, 'New York'])
print(mydict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(mydict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}