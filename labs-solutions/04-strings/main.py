# Step 1

original_string = 'John,Andrew,Smith,21,London,UK'
new_string = original_string.replace(',', ' ')
print(f"Original string =- '{original_string}'")
print(f"New string = '{new_string}'")

# Step 2
original_string_1 = input('Please input first string: ')
original_string_2 = input('Please input the second string: ')
new_string = original_string_1 + ' ' + original_string_2
print(new_string)

# Step 3
print(f'Length of new_string = {len(new_string)}')
upper_case_string = new_string.upper()
print(f'Upper case = {upper_case_string}')
print(f'The position of the string "albus" is : {new_string.find("Albus")}')
print(f'new_string == "hello World" : {new_string == "Hello World"}')
print(f'The value of string is {new_string}')

# Step 4
flag = True
count = 10
temperature = 32.6

flag_string = str(flag)
count_string = str(count)
temp_string = str(temperature)

print(f"flag = '{flag}' with type {type(flag)}")
print(f"count = '{count}' with type {type(count)}")
print(f"temperature = '{temperature}' with type {type(temperature)}")

print('-' * 25)

print(f"count_string = '{count_string}' with type {type(count_string)}")
print(f"temp_string = '{temp_string}' with type {type(temp_string)}")
print(f"flag_string = '{flag_string}' with type {type(flag_string)}")

# Step 5 (Optional)
distance_in_km = int(input('Please input the distance in kilometres: '))
distance_in_miles = distance_in_km * 0.6214
print(f'The distance in miles is {distance_in_miles}')
