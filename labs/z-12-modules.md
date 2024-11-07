### Lab: Working with Imports and the `os` Module

**Objective**: Use imports to organize code into modules, and practice common `os` module operations for file and directory management.

---

### Part 1: Setup

1. **Create a New Folder**: In your project directory, create a folder called `file_manager_lab`.

2. **Create a Script for the Main Program**:
   - Inside `file_manager_lab`, create a Python file named `main.py`.
   
3. **Create a Utility Module**:
   - In the same folder, create a new file called `file_utils.py`.
   - This module will contain helper functions to work with files and directories.

---

### Part 2: Writing the Utility Functions in `file_utils.py`

In `file_utils.py`, define the following functions:

1. **Get Current Working Directory**:
   ```python
   import os

   def get_current_directory():
       """Returns the current working directory."""
       return os.getcwd()
   ```

2. **List Files in Directory**:
   ```python
   def list_files(directory):
       """Lists all files in the specified directory."""
       try:
           return os.listdir(directory)
       except FileNotFoundError:
           return "Directory not found."
   ```

3. **Create a New Directory**:
   ```python
   def create_directory(directory_name):
       """Creates a new directory with the specified name."""
       try:
           os.mkdir(directory_name)
           return f"Directory '{directory_name}' created successfully."
       except FileExistsError:
           return "Directory already exists."
   ```

4. **Delete a Directory**:
   ```python
   def delete_directory(directory_name):
       """Deletes the specified directory if it's empty."""
       try:
           os.rmdir(directory_name)
           return f"Directory '{directory_name}' deleted successfully."
       except FileNotFoundError:
           return "Directory not found."
       except OSError:
           return "Directory is not empty or cannot be deleted."
   ```

---

### Part 3: Using the Utility Functions in `main.py`

1. In `main.py`, import the functions from `file_utils.py` and use them in a simple menu-based program.

   ```python
   # main.py

   from file_utils import get_current_directory, list_files, create_directory, delete_directory

   def main():
       while True:
           print("\nFile Manager")
           print("1. Show current directory")
           print("2. List files in directory")
           print("3. Create a new directory")
           print("4. Delete a directory")
           print("5. Exit")
           
           choice = input("Enter your choice: ")
           
           if choice == '1':
               print("Current Directory:", get_current_directory())
           
           elif choice == '2':
               directory = input("Enter directory to list files: ")
               print("Files:", list_files(directory))
           
           elif choice == '3':
               directory_name = input("Enter new directory name: ")
               print(create_directory(directory_name))
           
           elif choice == '4':
               directory_name = input("Enter directory name to delete: ")
               print(delete_directory(directory_name))
           
           elif choice == '5':
               print("Exiting the File Manager.")
               break
           
           else:
               print("Invalid choice, please try again.")

   if __name__ == "__main__":
       main()
   ```

---

### Part 4: Run the Program

1. Run `main.py` to start the file manager program.
2. Test each option by creating, listing, and deleting directories.

### Summary

This lab teaches you to:
- Use `os` functions for file and directory management.
- Organize functions in a separate module and import them in a main program.
- Use simple error handling to handle common filesystem issues.

This setup provides a practical introduction to imports and the `os` module with common directory operations.
