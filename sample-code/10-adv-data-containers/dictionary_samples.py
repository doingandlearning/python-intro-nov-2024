empty_dictionary = {}

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}

print(cities)

print('cities[Wales]:', cities['Wales'])
print('cities.get(Ireland):', cities.get('Ireland'))
print(cities.values())
print(cities.keys())
print(cities.items())
print('Wales' in cities)
print('France' not in cities)

for country in cities:
    print(country, end=', ')
    print(cities[country])

del cities['Scotland']  # Delete
cities['France'] = 'Paris'  # Add
cities['Wales'] = 'Swansea'  # Replace
