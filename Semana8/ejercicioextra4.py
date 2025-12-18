def write_function(path) :
    entry = input("Ingrese el texto a agregar al archivo : ")
    with open(path,"a",encoding="utf-8") as file:
        file.write(entry + "\n")


write_function("file.log")

