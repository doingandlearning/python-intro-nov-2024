num = input("Please enter a number: ")

if num.startswith("-"):
    print("You must enter a positive distance")
else:
    if num.replace(".", "", 1).isnumeric():
        num = float(num)
        if num < 0:
            print("You must enter a positive distance")
        else:
            print(f"You entered the distance {num} in kilometers")
            print(f"That is {num * 0.6214} in miles")
    else:
        print("Whoops! You need to give me a number.")
