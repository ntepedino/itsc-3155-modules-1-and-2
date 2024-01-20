# excercise 4
n = int(input("Enter the number of floats: "))

numbers = [float(input(f"Enter float {i + 1}: ")) for i in range(n)]

print("List:", numbers)
mean = sum(numbers) / n
print("Mean:", mean)