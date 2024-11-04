greeting = "Hello"
name = "Gert"

print(greeting + " " + name)  # use + symbol to concatenate

print(name.find("er"))  # if it exists, where does it start?
print("This is a longer string".find("long"))
# Gert
# 0123

print("It is raining outside.".replace("raining", "sunny"))
print(greeting.startswith("G"))

print("Kevin" == "   Kevin   ".strip())

print("I love cheese".find("chocolate"))