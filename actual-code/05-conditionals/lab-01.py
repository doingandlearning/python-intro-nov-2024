num = input("Please enter a number: ")

# if num.isnumeric() or num.startswith("-"):

if num.isnumeric() or (num.startswith("-") and num[1:].isnumeric()):
    num = int(num)
    if num < 0:
        print("Number is negative")
    elif num > 0:
        print("Number is positive")
    else:
        print("Number is zero")
else:
    print("Whoops! You need to give me a number.")


