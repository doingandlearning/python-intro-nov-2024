print('Starting factorial calculation program')
number = input('Please input the number: ')  # as a string!

if number == "0":
    print(f"The factorial of 0 is 1.")
elif number.isnumeric():
    print(f'The number to calculate factorial for is {number}')
    number = int(number)
    result = 1
    for i in range(number):
        result = result * (i + 1)
    print(f"The factorial of {number} is {result:,}.")
else:
    print('Not a positive integer number')