from datetime import datetime

print('Creating file')

with open('date_file.txt', 'w') as file:
    print('Writing date information to file')
    todays_date = str(datetime.today())
    file.write(todays_date)

print('Done')
