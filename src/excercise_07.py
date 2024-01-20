# excercise 7
numbers = []
while True:
    user_input = input("Enter an integer (type 'QUIT' to stop): ")
    if user_input.upper() == "QUIT":
        break
    numbers.append(int(user_input))

even_numbers = [num for num in numbers if num % 2 == 0]

print("All Numbers:", numbers)
print("Even Numbers:", even_numbers)
