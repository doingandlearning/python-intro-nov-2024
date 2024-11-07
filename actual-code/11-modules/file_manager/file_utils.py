import os


def get_current_directory():
    """Returns the current working directory."""
    return os.getcwd()


def list_files(directory):
    """Lists all files in the specified directory."""
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return "Directory not found."


def create_directory(directory_name):
    """Creates a new directory with the specified name."""
    try:
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created successfully."
    except FileExistsError:
        return "Directory already exists."


def delete_directory(directory_name):
    """Deletes the specified directory if it's empty."""
    try:
        os.rmdir(directory_name)
        return f"Directory '{directory_name}' deleted successfully."
    except FileNotFoundError:
        return "Directory not found."
    except OSError:
        return "Directory is not empty or cannot be deleted."