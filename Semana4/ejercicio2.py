input("Ingrese su nombre:")
input("Ingrese su apellido:")
age=int(input("Ingrese su edad:"))
if age<=3:
    print("Usuario es bebe")
elif age>3 and age<=10:
    print("Usuario es niño")
elif age>10 and age<=13:
    print("Usuario es preadolescente")
elif age>13 and age<=18:
    print("Usuario es adolescente")
elif age>18 and age<=25:
    print("Usuario es adulto joven")
elif age>25 and age<65:
    print("Usuario es adulto")
else:
    print("Usuario es adulto mayor")
