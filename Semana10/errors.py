
class InvalidNameError(Exception):
    pass


class GradeOutOfRangeError(Exception):
    pass

class InvalidSectionError(Exception):
    pass

def review_valid_input(input):
    try:
        number = int(input)
    except ValueError:
        raise ValueError("Usted ingreso un valor incorrecto, intente de nuevo")
    
    if number <= 0:
        raise ValueError("La cantidad debe ser mayor a cero.")
    
    return number

def review_grade(grade):
    try:
        grade = float(grade)
    except ValueError:
        raise ValueError("La nota no puede llevar letras,intente de nuevo")

    if grade < 0 or grade > 100:
        raise GradeOutOfRangeError("La nota debe estar entre 0 y 100, intente de nuevo")

    return "Nota válida"

            

def review_valid_name(name):
    name = name.strip()
    if name == "":
        raise InvalidNameError("El nombre no puede estar en blanco, intente de nuevo")
    
    if any(char.isdigit() for char in name):
        raise InvalidNameError("El nombre no puede contener números, intente de nuevo")

    return name


def review_valid_section(section):
    if len(section) != 2 and len(section) != 3:
        raise InvalidSectionError("La sección ingresada no cumple con el formato requerido, debe ingresar la sección en el siguiente formato: 11A, debe contener al menos un numero y una letra")
    valid_numbers_in_section = range(1,13)
    valid_letters_in_section = ["A","B","C","D","E","F"]
    numeric_part = section[:-1]
    alpha_part = section[-1]
    if not all(char.isalpha() for char in alpha_part):
        raise InvalidSectionError("La sección ingresada no cumple con el formato requerido, debe ingresar la sección en el siguiente formato: 11A")
    if not all(char.isupper() for char in alpha_part):
        raise InvalidSectionError("La letra de sección debe ir en mayúscula")
    if alpha_part not in valid_letters_in_section:
        raise InvalidSectionError("Letra de sección inválida, solo letras desde la A hasta la F son válidas" )
    if not all(char.isdigit() for char in numeric_part):
        raise InvalidSectionError("La sección ingresada no cumple con el formato requerido, debe ingresar la sección en el siguiente formato: 11A")
    if int(numeric_part) not in valid_numbers_in_section:
        raise InvalidSectionError("Número de sección inválida, solo números del 1 al 12 son válidos")
    
    return section
    
    
        




