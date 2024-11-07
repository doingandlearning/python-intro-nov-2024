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