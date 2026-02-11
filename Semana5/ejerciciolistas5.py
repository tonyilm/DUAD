while True:
    my_numbers = input("Ingrese 10 números separados por coma: ").split(",")

    if len(my_numbers) == 10:
        my_numbers = list(map(int, my_numbers))
        greatest_number = max(my_numbers)
        print(f"{my_numbers} El más alto fue {greatest_number}")
        break
        
    else:
        print("Debe ingresar 10 números.")
 
