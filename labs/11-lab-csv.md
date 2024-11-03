# Lab 11: Working with CSV Files

In this lab, you will create a CSV file based on a set of temperature readings taken from a sensor.

---

## Objective

1. Use a tuple of tuples to represent a series of temperatures. For example:

   ```python
   temperatures = (
       (10.05, '04/05/23', '12:00', 'Celsius'),
       (11.00, '04/05/23', '13:00', 'Celsius'),
       (12.34, '04/05/23', '14:00', 'Celsius'),
       (11.95, '04/05/23', '15:00', 'Celsius'),
       (9.25, '04/05/23', '16:00', 'Celsius'),
   )
   ```

   - Each inner tuple represents a temperature reading with the reading, date, time, and scale.

2. Create a function (e.g., `write_to_csv()`) that takes an iterable (such as a tuple of tuples) and writes the data to a CSV file.

   - Example usage:

     ```python
     print('Starting')
     print('Writing Temperature Data')
     write_to_csv('temperatures.csv', temperatures)
     print('Done')
     ```

3. Sample `write_to_csv` function outline:

   ```python
   import csv

   def write_to_csv(filename, data):
       print('Starting write of CSV example')
       with open(filename, 'w', newline='') as csvfile:
           writer = csv.writer(csvfile)
           # Write out the data
           # Your code goes here
   ```

---

## Extension Point

1. Write another program to reload the values from the CSV file into a new tuple and print out each tuple.

2. Use `csv.reader` to read the CSV file, for example:

   ```python
   import csv

   with open('temperatures.csv') as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
           # Your code goes here
   ```

3. Example output:

   ```
   Loading file temperatures.csv
   Finished reading file
   [['10.05', '04/05/23', '12:00', 'Celsius'], ['11.0', '04/05/23', '13:00', 'Celsius'], ['12.34', '04/05/23', '14:00', 'Celsius'], ['11.95', '04/05/23', '15:00', 'Celsius'], ['9.25', '04/05/23', '16:00', 'Celsius']]
   ```
