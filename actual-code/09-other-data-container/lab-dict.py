flights = {
    'London': ('EY123', 'Monday', '12:00', 'Geneva'),
    'Geneva': ('AI454', 'Tuesday', '13:00', 'London'),
    'Dublin': ('BA987', 'Wednesday', '14:00', 'Dublin'),
    'Seville': ('SA527', 'Thursday', '11:00', 'Cardiff'),
    'Cardiff': ('WA129', 'Friday', '10:00', 'Dublin')
}

# Print out all the keys.
print(flights.keys())
# Print out all the values.
print(flights.values())
# Find the flight associated with a particular city (e.g., Dublin).
print(flights["Dublin"])
# Add a new flight for France to the dictionary and print out all the key-value pairs. The flight for France could be ('AF429', 'Saturday', '09:00', 'London').
flights["France"] = ('AF429', 'Saturday', '09:00', 'London')
print(flights)
# Remove the flight from the dictionary for Cardiff and reprint all items.
del flights["Cardiff"]
print(flights)
