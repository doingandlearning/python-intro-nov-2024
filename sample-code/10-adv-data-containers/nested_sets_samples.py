s1 = {(1, 2, 3)}
print(s1)

# Need to convert sets to frozensets
s2 = {frozenset({1, 2, 3})}
print(s2)

s3 = {tuple([1, 2, 3, 2, 1])}
print(s3)
