def calculator():
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        operation = input('Enter an operation (+, -, *, /): ')

        if operation == '+':
            result = num1 + num2
            print(f'{num1} + {num2} = {result}')
        elif operation == '-':
            result = num1 - num2
            print(f'{num1} - {num2} = {result}')
        elif operation == '*':
            result = num1 * num2
            print(f'{num1} * {num2} = {result}')
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f'{num1} / {num2} = {result}')
            else:
                print('Error: Division by zero is not allowed.')
        else:
            print('Error: Invalid operation.')
    except ValueError:
        print('Error: Please enter valid numbers.')

calculator()
