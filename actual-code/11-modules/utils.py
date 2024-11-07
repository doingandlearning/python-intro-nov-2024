def add(a, b):
    return a + b

name = "Kevin"


def main():
    print("I am from the utils.py file")
    print(add(1, 2))
    print(__name__)  # dunder -> double underscore

if __name__ == "__main__":
    main()
    print("I am from the utils.py file")
    print(add(1, 2))
    print(__name__)  # dunder -> double underscore