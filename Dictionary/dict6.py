dictionary = {
  "brand": "MTJ",
  "electric": False,
  "year": 2023,
  "color": ["Yellow", "white", "blue"]
}
dictionary["year"] = 2002
print(dictionary)
dictionary.update({"brand": "LimeLight"})
print(dictionary)
dictionary["color"] = "red"
print(dictionary)