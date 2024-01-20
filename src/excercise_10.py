# excercise 10
input_string = input("Enter a string: ")
characters = list(input_string)

nested_lists = [characters[i:i + 3] for i in range(0, len(characters), 3)]

print("List of Characters:", characters)
print("List of Lists:", nested_lists)

