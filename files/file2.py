file = "text.txt"
with open(file, 'r') as f:
    lines = f.readlines()
for x in lines:
    print(x)
