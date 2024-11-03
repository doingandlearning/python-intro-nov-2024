# Lab 3: Types

The aim of this lab is to extend our hello world application to make it interactive and to handle different types of data.

This lab is comprised of 5 steps:

- Make the application interactive
- Input some numbers
- Input some strings
- Concatenate numbers and strings

---

## Step 1: Make the Application Interactive

1. Modify your program to take user input as shown in the lecture slides.

   An example of the interaction between the program and the user is shown below:

   ```
   Hello World!
   Please enter your name: John
   Welcome John
   ```

2. To do this, follow the style of application presented in the notes. For example:

   ```python
   # Print out a message and then ask the user for input
   print('Hello, World')
   user_name = input('Enter your name: ')
   print('Welcome', user_name)
   ```

3. Now add some comments to explain what you have just done.

---

## Step 2: Input Some Numbers

1. In this step, ask the user for two numbers.

   - Note that the result returned from the `input()` function is a string. You must convert the input string into a number. This can be done using the `int()` function, which converts a string (or a float) into an integer. Similarly, the `float()` function will convert an int or a string into a float, and the `str()` function converts int and float into strings, etc.

   ```python
   input1 = int(input('Please enter a number: '))
   input2 = int(input('Please enter another number: '))
   ```

2. Next, add the two numbers together and then print out the result.

   ```python
   value = input1 + input2
   print('The result of', input1, '+', input2, 'is', value)
   ```

3. Run the program and confirm the output, for example:

   ```
   Please enter a number: 2
   Please enter another number: 3
   The result of 2 + 3 is 5
   ```

4. Finally, print out the type of the variable holding the result:

   ```python
   print('The type of the value is', type(value))
   ```

---

## Step 3: Input Two Strings

1. Ask the user to input two strings, for example:

   ```python
   input_string1 = input('Please enter a string: ')
   input_string2 = input('Please enter another string: ')
   ```

2. Use the `+` operator to concatenate the two strings and print out the result:

   ```python
   value = input_string1 + input_string2
   print('The new value is', value)
   ```

3. Next, print out the type of the variable `value` after the above assignment. What is its type now?

---

## Step 4: Concatenate a Number and a String

1. Use the add operator to add a version number to your application.

   ```python
   title = 'Data Processing App Version ' + str(1.0)
   print('The title of this app is', title)
   ```

2. Add the above code and rerun your application. What is the result?

3. Now, remove the `str(1.0)` and replace it with just `1.0` – rerun the program. What happens?

4. Return the code to use `str(1.0)`.
