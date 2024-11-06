#! python3

from datetime import datetime
import sys

def log_message(text_message):
    message = f"{datetime.now()}: {text_message}"

    with open("log.txt", "a") as f:
        f.write(f"{message}\n")


log_message(sys.argv[1])
