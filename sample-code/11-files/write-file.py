print('Writing file')

with open('myfile2.txt', 'w') as f:
    f.write('Hello from Python!!\n')
    f.write('Working with files is easy...\n')
    f.write('It is cool ...\n')
    f.write(str(42))  # Note write takes a string

print('Done')
