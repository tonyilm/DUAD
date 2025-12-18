counter=1
import random
random_number=random.randint(1,10)
print("Tiene 10 intentos para adivinar el numero secreto")
while counter<=10:
    number=int(input("Ingrese su numero a adivinar entre 1 y 10:"))
    if number<=10 and number>=1:
        if number==random_number:
            print(f"Felicitaciones, ha adivinado el numero secreto({random_number})")
            break
        else:
            print("Intente de nuevo")
            counter=counter+1
    else:
        print("Debe ingresar un numero del 1 al 10")
else:
    print(f"No adivinaste el numero dentro del limite de los 10 intentos, el numero secreto era:{random_number}")
