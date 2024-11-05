# 3.10 -> pattern matching

favorite_genre = input("What's your favorite movie genre? ").lower()

match favorite_genre:
    case "comedy":
        print("Let's watch Dumb and Dumber!")
    case "horror":
        print("Let's watch Get Out!")
    case "action":
        print("Let's John Wick!")
    case _:
        print("You suggest a movie then.")
