file = "text2.txt"
with open(file, 'r') as f:
    lines = f.readlines()
with open("text1.txt", 'w+') as f:
    for line in lines:
        f.write(line)