dictionary = {
  "brand": "MTJ",
  "electric": False,
  "year": 2023,
  "colors": ["Yellow", "white", "blue"]
}
print(type(dictionary))
print(dictionary)
x = dictionary["electric"]
print(x)
y = dictionary.keys()
print(y)
z = dictionary.values()
print(z)
dictionary["year"] = 2002
print(dictionary)
