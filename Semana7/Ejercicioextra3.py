def sum_values(list):
    result = 0
    for element in list:
        try:
            number = float(element)
            print(f"{number} added successfully")
            result =result + number
        
        except ValueError:
            print(f"Invalid element: {element} ")
    print(f"Total sum : {result}")                 

list = input("Enter the strings separated by commas : ").split(",")

sum_values(list)