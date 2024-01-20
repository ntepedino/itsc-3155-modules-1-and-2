# excercise 5
list1 = [int(input("Enter integer for list1: ")) for _ in range(5)]
list2 = [int(input("Enter integer for list2: ")) for _ in range(5)]

common_values = list(set(list1) & set(list2))

print("List1:", list1)
print("List2:", list2)
print("Common Values Without Duplicates:", common_values)