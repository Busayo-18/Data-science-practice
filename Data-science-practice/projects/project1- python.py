'''
#create a program that introduces yourself
#write a program to ask a user  3 questions and store the answers in variables
#write a simple calculator program that ask users for inputs and give answers
# write a program that collects input from users and 

'''



print('\n' + '=' *50)
print('TASK 1: Create a program that introduces yourself')
print('=' *50 + '\n')
name = 'Olagunju Amina'
skills =  ['Data Analysis','Data Visualization','and', 'Machine Learning']
career_path = 'Data Scientist'
print(f'Hello, my name is {name}. I am skilled in {", ".join(skills)}, and I aspire to be a {career_path}.')


print('\n' + '=' *50)
print('TASK 2: Create a program that asks 3 questions and store answers')
print('=' *50 + '\n')
name = input('What is your name:')
nationality = input('What country are you from:')
ethnicity = input('What is your ethnic group:')
print()
print('Thank you for your responses!')
print()
print('Name:', name)
print('Nationality:', nationality)
print('Ethnicity:', ethnicity)

print('\n' + '=' *50)
print('TASK 3: A simple calculator program asking users for inputs and giving results')
print('=' *50 + '\n')
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operation = input('Choose an operation (+, -, *, /): ')

if operation == '+':
    result = num1 + num2
elif operation == '-':  
    result = num1 - num2
elif operation == '*':
    result = num1 * num2    
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: Division by zero is not allowed.'
        
else:
    result = 'Error: Invalid operation selected.' # Handle invalid operation        
print()
print(f'{num1} {operation} {num2} = {result}') #displays result for operations(+,-,*,/)


print('\n' + '=' *50)
print('TASK 4: A program that collects input from users and displays it')
print('=' *50 + '\n')
name = input('What is your name:')
nationality = input('What country are you from:')
ethnicity = input('What is your ethnic group:')
print(f'Hi,your name is {name}. You are from {nationality} and you identify as {ethnicity}.')