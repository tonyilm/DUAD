def prime_number() :
    entry = input("Ingrese los numeros separados por coma : ").split(",")
    numbers_list = list(map(int,entry))
    prime_numbers = 0
    lista_de_primos = []
    for number in numbers_list:
            if number<=1:
                continue
            elif number == 2:
                prime_numbers = prime_numbers+1
                lista_de_primos.append(number)
            else:
                for i in range(2,number):
                    if number % i == 0:
                         break
                else:
                    prime_numbers = prime_numbers+1
                    lista_de_primos.append(number)
    print(f"Se encontraron {prime_numbers} numeros primos : :{lista_de_primos} ")
        
prime_number()