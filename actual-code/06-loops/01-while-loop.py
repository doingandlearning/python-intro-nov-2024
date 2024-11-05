count = 5

while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # count = count - 1

print("Liftoff! 🚀")

password = "opensesame"
guess = ""

while guess != password:
    guess = input("Enter the password: ")
    if guess == password:
        print("Access granted! 🔑")
    else:
        print("❌ Access denied. Try again.")