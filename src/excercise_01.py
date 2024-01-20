# excercise 1
grade = int(input("Enter a grade from 0 to 100: "))

if(grade < 100 and grade >= 90):
    letter = 'A'
elif(grade < 90 and grade >= 80):
    letter = 'B'
elif(grade < 80 and grade >= 70):
    letter = 'C'
elif(grade < 70 and grade >= 60):
    letter = 'D'
else:
    letter = 'F'

print (letter)