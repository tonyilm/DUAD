def string_function() :
    first_string = input("Ingrese el texto separado por guiones : ")
    my_list = first_string.split("-")
    my_list.sort()
    exit = "-".join(my_list)
    print(exit)


string_function()
