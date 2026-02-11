while True:
    my_list=input("Ingrese su lista de numeros separada por coma: ").split(",")
    if len(my_list)>=2:
        my_even_number_list=[]
        for number in my_list:
            number=int(number)
            if number % 2 == 0:
                my_even_number_list.append(number)
    print(my_even_number_list)
    break
else:
    print("Debe ingresar 2 o mas numeros")

