def char_function() :
    my_string = input("Ingrese el texto : ")
    my_character = input("Ingrese el caracter que desea buscar : ")
    char_counter = 0

    for char in my_string:
        if char == my_character:
            char_counter = char_counter+1
        else:
            continue
    print(f"Se ha encontrado {char_counter} veces el caracter")

char_function()
                