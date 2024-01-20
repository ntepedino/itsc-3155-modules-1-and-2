user_input = input("Enter string: ")

uCase, lCase = '', ''

for i in user_input:
    if i.isupper():
        uCase+=i
    elif i.islower():
        lCase+=i

print(''.join([lCase,uCase]))
