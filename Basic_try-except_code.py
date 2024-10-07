while True:
    try:
        age = int(input("Enter your age"))
        if age < 18:
            raise ValueError("Your age is under 18, you can't in.")
        print("You can go")
        break

    except ValueError as e:
        print(f"Error: {e},This is not good")
        continue
