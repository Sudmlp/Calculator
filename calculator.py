print('Hi! I am a calculator')

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

num1 = int(num1)
num2 = int(num2)

print('Perform one of these operations: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division')
option = input('Please enter your choice: ') 
option = int(option)

if option == 1:
    result = num1 + num2
    print('Addition: ', result)
elif option == 2:
    result = num1 - num2
    print('Subtraction: ', result)
elif option == 3:
    result = num1 * num2
    print('Multiplication: ', result)
elif option == 4:
    result = num1 / num2
    print('Division: ', result)
else:
    print('Invalid operation.')
    


