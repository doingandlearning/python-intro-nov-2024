empty_dictionary = {}

print(empty_dictionary)
print(type(empty_dictionary))

capital_dict = {   # dict
    "Poland": ("Warsaw", 1_794_166),       # Population as of latest estimate
    "France": ("Paris", 2_161_000),  # tuple
    "Italy": ("Rome", 2_860_009),
    "Uruguay": ("Montevideo", 1_319_108),
    "Netherlands": ("Amsterdam", 905_234)
}

print(capital_dict)
print(capital_dict["Poland"])
print(capital_dict.get("Uruguay"))  # giving the key, getting the value

capital_dict["Ireland"] = ("Dublin", 592_713)



# tuple_1[1:2]

user1 = ["Gert", "Netherlands", "Electrical Engineer"]
user2 = { "name": "Gert", "profession": "Electrical Engineer", "country_of_origin": "Netherlands"}

user3 = ["Gianluigi", "Engineer", "Italy"]

print(f"{user1[0]} is an {user1[2]} who is from {user1[1]}")
print(f"{user2["name"]} is an {user2["profession"]} who is from {user2["country_of_origin"]}")


print(user2.items())
print(user2.keys())
print(user2.values())

print(capital_dict.keys())

print(("Dublin", 592_713) in capital_dict) # membership is checked in the keys not the values.
print(capital_dict)
print(("Dublin", 592_713) in capital_dict.values())

for country in capital_dict:
    print(f"{country} has a capital city of {capital_dict[country][0]} with a population of {capital_dict[country][1]:,}.")

for capital in capital_dict.values():
    print(f"{capital[0]} has a population of {capital[1]:,}.")