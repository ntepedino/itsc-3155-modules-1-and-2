# excercise 6
row_num = int(input("Enter row number (1-5): "))
col_num = int(input("Enter column number (1-5): "))

for i in range(1, 6):
    for j in range(1, 6):
        if i == row_num and j == col_num:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
