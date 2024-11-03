empty_set = set()  # Empty set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print(len(basket))
for item in basket:
    print(basket)

print('apple' in basket)

basket.add('apricot')
print(item)

# Add more than one item at a time
basket.update(['apricot', 'mango', 'grapefruit'])
basket.remove('apricot')  # or discard

# Set like operations
s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}

# Union
print('Union:', s1 | s2)

# Intersection
print('Intersect:', s1 & s2)

# Difference
print('Difference:', s1 - s2)
