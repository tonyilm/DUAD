def word_function() :
    word_list = input("Ingrese las palabras separadas por coma : ").split(",")
    letter_number = int(input("Ingrese el numero de letras minimas en la palabra : "))
    new_list = []

    for word in word_list:
        if len(word)>= letter_number:
            new_list.append(word)
        

    if len(new_list) == 0:
        print("Ninguna palabra de la lista cumple con el numero minimo de caracteres")
    else:
        print(new_list)


word_function()
    
