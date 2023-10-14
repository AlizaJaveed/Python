def SumEven(num):
    sum = 0
    for j in num:
        if j % 2 == 0:
            sum += j
    return sum
count = int(input("Enter the num of elements in the list: "))
num = []
for i in range(count):
    num1 = int(input(f"Enter element {i + 1}: "))
    num.append(num1)
Even = SumEven(num)
print("Entered list:", num)
print("Sum of even number:", Even)
