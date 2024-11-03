distance_in_km_str = input('Please input the distance in kilometres: ')

distance_in_km_str = distance_in_km_str.replace(' ', '')

if distance_in_km_str.startswith('-'):
    print('You must enter a positive distance')
elif distance_in_km_str.isalpha():
    print('Cant be letters')
else:
    if distance_in_km_str.count('.') < 2 and distance_in_km_str.replace('.','').isnumeric():
        # Its a floating point number - possibly
        distance_in_km = float(distance_in_km_str)
    elif distance_in_km_str.isnumeric():
        distance_in_km = int(distance_in_km_str)

    print(f'You entered the distance {distance_in_km} in kilometres')
    distance_in_miles = distance_in_km * 0.6214
    print(f'The distance in miles is {distance_in_miles:.4f}')

