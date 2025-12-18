while True:
    name = input("Enter your name : ")
    if name.isdigit():
        raise ValueError("Name cannot be a number")
        continue
    try:
        age = int(input("Enter your age : "))
    except ValueError as e:
        print(f"You must enter a numeric value, invalid number. Details: {e}")
        continue
    if age in range(0,120):
        print(f"Hello {name}, your age is {age}")
    else:
        print("Invalid age")


    