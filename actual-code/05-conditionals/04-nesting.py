temperature_outside = -2
is_snowing = True
is_ski_season = True

print(f"The temperature is {temperature_outside} degrees celcius")


if temperature_outside < 0:   # the test can be anything -> but it has to be True or False
    print("Put on a coat.")
    print("It is freezing.")
    if is_snowing:
        print("Put on some boots!")
        if is_ski_season:
            print("Let's call in sick to work!")
        else:
            print("I guess we'll go to work!")
    print("Time for hot chocolate!")

print("Let's go outside!")

