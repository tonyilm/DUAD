while True:
    my_list=input("Ingrese su lista de elementos separados por coma: ").split(",")
    if len(my_list)>=2:
        my_list[0],my_list[-1] = my_list[-1],my_list[0]
        print(my_list)
        break
    else:
        print("Debe ingresar 2 o mas elementos")