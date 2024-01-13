import random
import time

def numbers():
    num1 = random.randrange(3, 11)
    num2 = random.randrange(3, 11)
    return num1, num2

def operate(num1, num2):
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        if num1 > num2:
            result = num1 - num2
        else: 
            result = num2 - num1
    return operator, result

input("\nPress 'Enter' to start >> ")
print('-----------------------')
start_time = time.time()

i = 0
total = 0

while i < 10:
    num1, num2  = numbers()
    operator, result = operate(num1, num2)

    if num1 > num2 and operator == '-':
        calculate = input(f'{num1} {operator} {num2} = ')
    else:
        calculate = input(f'{num2} {operator} {num1} = ')

    if result == int(calculate):
        print('Correct!')
        total += 1
    else:
        print('Wrong!')

    i += 1
    
    end_time = time.time()

print(f"Your score : {total}\nAccuracy : {total*10}%\nYou've finished in {round(end_time - start_time)} seconds")


