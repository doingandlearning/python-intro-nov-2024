# () tuple
# [] list
# {} dictionary
# {} set

empty_set = set()
print(empty_set)
print(type(empty_set))

fruit_set = {"apple", "orange", "pear", "banana", "orange", "apple"}
print(fruit_set)
print(type(fruit_set))

print(len(fruit_set))

print("kiwi" in fruit_set)  # check for membership
fruit_set.add("kiwi")  # add an element
print("kiwi" in fruit_set)

fruit_set.update(["dragon fruit", "plum", "grapes", "banana"])
print(fruit_set)

fruit_set.remove("dragon fruit")
print(fruit_set)

# Using a set to de-duplicate a list
set_of_favorite_movies = set(["Matrix", "Bad Boys", "Walle", "Luca", "Walle", "Matrix", "Matrix", "banana"])

print(fruit_set.intersection(set_of_favorite_movies))
print(fruit_set & set_of_favorite_movies)

print(fruit_set.union(set_of_favorite_movies))
print(fruit_set | set_of_favorite_movies)

print(fruit_set.difference(set_of_favorite_movies))
print(fruit_set - set_of_favorite_movies)