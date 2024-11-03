import csv

temperatures = (
        (10.05, '04/05/23', '12:00', 'Celsius'),
        (11.00, '04/05/23', '13:00', 'Celsius'),
        (12.34, '04/05/23', '14:00', 'Celsius'),
        (11.95, '04/05/23', '15:00', 'Celsius'),
        (9.25, '04/05/23', '16:00', 'Celsius'),
)


def write_to_csv(filename, data):
    print('Starting write of CSV example')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        # Write out the transactions
        for item in data:
            writer.writerow(item)


print('Starting')

print('Writing Temperature Data')
write_to_csv('temperatures.csv', temperatures)

print('Done')
