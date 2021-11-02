# 30 DAYS CODING CHALLENGE
# 1ST 02-11-2021
# Did a caracter counter


text = str(input(f"Enter your text here: -> "))
letterList, numList, otherList = [], [], []
letter, num, other = 0, 0, 0

for i in text:
    if str.isalpha(i):
        letter += 1
        letterList.append(i)
    elif str.isdigit(i):
        num += 1
        numList.append(i)
    elif i != " ":
        other += 1
        otherList.append(i)

    
print(f"Your text as {letter + num + other} caractere")
print(f"You have {letter} letter, {num} numbers and {other} other caracteres")