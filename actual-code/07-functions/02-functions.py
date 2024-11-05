def add(number1, number2):
    print(number1 + number2)

add(1,2)

def print_area_of_rectangle(length, width):
    # Many lines!
    print(length * width)

print_area_of_rectangle(4,5)

def greeting(name, greeting="How are you?"):
    print(f"{name}, {greeting}")

greeting("Maxime", "Comment vas-tu?")
greeting("Gianluigi", "Come stai?")
greeting("Krzysztof", "Jak sie masz")
greeting("Kevin")

def print_temperature_reading(value, unit="C", time="now"):
    print(f"The reading was {value}{unit} at time {time}")

print_temperature_reading(time="13:55", value=8)
print_temperature_reading(10, "F")