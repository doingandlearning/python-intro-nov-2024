def add(num1, num2):
    if type(num1) is not int or type(num2) is not int:  # defensive programming
        return "Tried to add non-numbers. Try again."
    return num1 + num2

result = add(2,"3")
print(result)