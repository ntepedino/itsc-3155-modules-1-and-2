# excercise 8
numbers = [int(input(f"Enter integer {i + 1}: ")) for i in range(10)]

unique_numbers = [num for num in numbers if numbers.count(num) == 1]

print("All Numbers:", numbers)
print("Unique Numbers:", unique_numbers)
