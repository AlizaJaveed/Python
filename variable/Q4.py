friends = ["Aliza", "kinza", "maria"]
print(friends)
for i in range(len(friends)):
    print(friends[i])
    
# Function to calculate the sum of even numbers in a list
def sum_of_even_numbers(numbers):
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum

# Get user input to create a list of numbers
try:
    num_count = int(input("Enter the number of elements in the list: "))
    numbers = []

    for i in range(num_count):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)

    # Calculate the sum of even numbers in the list
    even_sum_result = sum_of_even_numbers(numbers)

    # Display the list and the sum of even numbers
    print("Entered list:", numbers)
    print("Sum of even numbers:", even_sum_result)

except ValueError:
    print("Invalid input. Please enter valid integers for the list.")
