num = input("Please enter a number: ")

if num.isnumeric() or (num.startswith("-") and num[1:].isnumeric()):
    num = int(num)
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("Whoops! You need to give me a number.")
