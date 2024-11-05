age = 27
# status = None   # Placeholder ... empty type

# if age > 12:
#     if age < 20:
#         status = "teenager"
#     else:
#         status = "not teenager"
# else:
#     status = "not teenager"

if age > 12 and age < 20:
    status = "teenager"
else:
    status = "not teenager"

print(status)

is_game_still_running = True

if is_game_still_running:
    print("Are you less grumpy?")