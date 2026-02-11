def convert_to_int(list):
    print("Result:")
    for element in list:
            try:
                number = int(element)
                print(f"{element} converted to {number}")
                   
            except ValueError:
                print(f"The following element could not be converted: {element}")
    
list = input("Enter the strings separated by commas : ").split(",")

convert_to_int(list)
    