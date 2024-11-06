# Lab 9: Sets and Dictionaries

Choose one of the activities to implement – if you have time, move on to the other activity.

---

## Activity 1: Sets

The aim of this activity is to use a **Set**.

1. Create two sets of students: one for those who took an exam and one for those who submitted a project. Use simple strings to represent the students, for example:

   ```python
   # Set up sets
   exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
   project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}
   
   # Output the basic sets
   print('exam:', exam)
   print('project:', project)
   ```

2. Using these sets, answer the following questions:

   - Which students took both the exam and submitted a project?
   - Which students only took the exam?
   - Which students only submitted the project?
   - List all students who took either (or both) of the exam and the project.
   - List all students who took either (but not both) of the exam and the project.

---

## Activity 2: Dictionaries

1. Create a dictionary to represent flights from cities around Europe.

   - The key should be a city.
   - The values should be a tuple containing the flight number, day of the week, time of the flight, and destination (all as strings).

   ```python
   flights = {
       'London': ('EY123', 'Monday', '12:00', 'Geneva'),
       'Geneva': ('AI454', 'Tuesday', '13:00', 'London'),
       'Dublin': ('BA987', 'Wednesday', '14:00', 'Dublin'),
       'Seville': ('SA527', 'Thursday', '11:00', 'Cardiff'),
       'Cardiff': ('WA129', 'Friday', '10:00', 'Dublin')
   }
   ```

2. Perform the following tasks:

   - Print out all the keys.
   - Print out all the values.
   - Find the flight associated with a particular city (e.g., Dublin).
   - Add a new flight for France to the dictionary and print out all the key-value pairs. The flight for France could be `('AF429', 'Saturday', '09:00', 'London')`.
   - Remove the flight from the dictionary for Cardiff and reprint all items.

3. Sample output:

   ```
   Keys: dict_keys(['London', 'Geneva', 'Dublin', 'Seville', 'Cardiff'])
   Values: dict_values([('EY123', 'Monday', '12:00', 'Geneva'), ('AI454', 'Tuesday', '13:00', 'London'), ('BA987', 'Wednesday', '14:00', 'Dublin'), ('SA527', 'Thursday', '11:00', 'Cardiff'), ('WA129', 'Friday', '10:00', 'Dublin')])

   The flight for Dublin is ('BA987', 'Wednesday', '14:00', 'Dublin')

   All key-value pairs: dict_items([('London', ('EY123', 'Monday', '12:00', 'Geneva')), ('Geneva', ('AI454', 'Tuesday', '13:00', 'London')), ('Dublin', ('BA987', 'Wednesday', '14:00', 'Dublin')), ('Seville', ('SA527', 'Thursday', '11:00', 'Cardiff')), ('Cardiff', ('WA129', 'Friday', '10:00', 'Dublin')), ('France', ('AF429', 'Saturday', '09:00', 'London'))])

   Removing the Cardiff flight
   All key-value pairs: dict_items([('London', ('EY123', 'Monday', '12:00', 'Geneva')), ('Geneva', ('AI454', 'Tuesday', '13:00', 'London')), ('Dublin', ('BA987', 'Wednesday', '14:00', 'Dublin')), ('Seville', ('SA527', 'Thursday', '11:00', 'Cardiff')), ('France', ('AF429', 'Saturday', '09:00', 'London'))])
   ```


### Extensions for Activity 1: Sets

1. **Top Performers**:
   - Assume the students who took both the exam and submitted a project are top performers.
   - Create a new set of "Top Performers" containing these students, and print it.
   
2. **Counting Participation**:
   - Count how many students participated in either the exam or the project. Print the total unique count.

3. **Comparing with Another Class**:
   - Introduce a new set representing students from another class who only took the exam.
   - Print which students are common between the two classes.
   - Print students who are unique to each class.

4. **Add Extra Students**:
   - Allow the user to add a new student to each of the "exam" and "project" sets.
   - Print out the updated sets and any changes in students who completed both or only one of the activities.

5. **Set Symmetry Check**:
   - Check if both sets have the same number of students.
   - If not, print which set has more participants.

---

### Extensions for Activity 2: Dictionaries

1. **Flight Schedule by Destination**:
   - Create a reverse lookup dictionary where each destination is a key, and the value is a list of all flights that go to that destination.
   - Print the dictionary to show which cities have flights heading to the same destination.

2. **Finding Flights on a Specific Day**:
   - Ask the user to enter a day of the week.
   - Print out all flights that depart on that day, showing the city, time, and destination.

3. **Time Zone Adjustments**:
   - Assume each flight is in local time and needs to be converted to UTC.
   - Adjust each time by a random offset (simulating different time zones) and print the new schedule.

4. **Updating a Flight Schedule**:
   - Prompt the user to update the details of a flight, such as changing the time or destination for a city.
   - After updating, print the full schedule to show the change.

5. **Flight Connections**:
   - Create a function that checks if there is a connecting flight from one city to another within the next two hours.
   - For instance, if a flight from London arrives in Geneva at 12:00, check if there’s another flight departing from Geneva before 14:00.
   - Print out any connections found for cities with flights close to each other.
