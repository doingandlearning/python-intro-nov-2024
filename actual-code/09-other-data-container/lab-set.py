# Set up sets
exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

# Output the basic sets
print('exam:', exam)
print('project:', project)

print(exam.intersection(project))
print(exam & project)
intersection = exam & project

everyone = exam.union(project)
print(exam.union(project))
print(exam | project)

print(everyone - intersection)