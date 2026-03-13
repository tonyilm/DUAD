import csv
import os
import data
from errors import review_grade, GradeOutOfRangeError,review_valid_name,InvalidNameError,review_valid_section,InvalidSectionError,review_valid_input

def add_new_student_to_CSV(file_path) :
    while True:
        try:
            number_of_students = input("Ingrese la cantidad de estudiantes que desea agregar : ")
            number_of_students = review_valid_input(number_of_students)
            break
        except ValueError as e:
            print(f"Error : {e}")
            
    student_list = []
        
        
    for student in range(number_of_students):
        print(f"Ingresando estudiante numero {student+1}")
        while True:   
            try:
                nombre_completo = input("Nombre completo: ")
                print(review_valid_name(nombre_completo))
                break
            except InvalidNameError as e:
                print(f"Error: {e}")
        while True:   
            try:
                seccion = input("Sección: ")
                print(review_valid_section(seccion))
                break
            except InvalidSectionError as e:
                print(f"Error: {e}")       
        while True:    
            try:
                
                nota_de_espanol = float(input("Nota de español: "))
                print(review_grade((nota_de_espanol)))
                break
            except ValueError as e:
                print(f"Error : {e} ")
            except GradeOutOfRangeError as e:
                print(f"Error: {e}")
        while True:    
            try:
                nota_de_ingles = float(input("Nota de ingles: "))
                print(review_grade(nota_de_ingles))
                break
            except ValueError as e:
                print(f"Error : {e} ")
            except GradeOutOfRangeError as e:
                print(f"Error: {e}")
        while True:
            try:
                nota_de_sociales = float(input("Nota de sociales: "))
                print(review_grade(nota_de_sociales))
                break
            except ValueError as e:
                print(f"Error : {e} ")   
            except GradeOutOfRangeError as e:
                print(f"Error: {e}")
        while True:
            try:
                nota_de_ciencias = float(input("Nota de ciencias: "))
                print(review_grade(nota_de_ciencias))
                break
            except ValueError as e:
                print(f"Error : {e} ")
            except GradeOutOfRangeError as e:
                print(f"Error: {e}")
       
        
    

        new_student = {
            "Nombre completo": nombre_completo,
            "Sección": seccion,
            "Nota de español" : nota_de_espanol,
            "Nota de inglés": nota_de_ingles,
            "Nota de sociales": nota_de_sociales,
            "Nota de ciencias": nota_de_ciencias
        }     
        
        

        student_list.append(new_student)
        print("Se agregó los estudiantes con éxito")

    if student_list:
        headers = list(student_list[0].keys())
        data.export_students_to_csv(file_path,student_list,headers)
        print("¡Datos exportados con éxito!")
        print("\n") 



def view_existing_student(file_path):
    print("Información de estudiantes existentes\n")
    students = data.import_all_students(file_path)
        
    if not students:
        print("No hay estudiantes registrados o el archivo no existe.")
        return
    for index, student in enumerate(students, start=1):
                print(f"Estudiante número {index} \n-------------------------------------")
                
                for key, value in student.items():
                    print(f"{key}: {value}")
                print("\n") 
              
          
def view_top_three(file_path):
        print("Top 3 estudiantes con mejor nota promedio :\n")
        students = data.import_all_students(file_path)
        
        average_list = []

        for row in students:
            total = 0
            grade_counter = 0
            for key,value in row.items():
                    if key != "Nombre completo" and key != "Sección":
                         grade = float(value)
                         total = total+grade
                         grade_counter = grade_counter+1
            average = total/grade_counter
            full_name = row["Nombre completo"]
            average_list.append((full_name,average))
        top_3_list = sorted(average_list, key=lambda x: x[1], reverse=True) [:3]
        
        for i, (name, average) in enumerate(top_3_list, start=1):
             print(f"{i}. {name} : {average:}")
        print("\n")


def view_student_average(file_path):
        students = data.import_all_students(file_path)
        print("Nota promedio de estudiantes :\n")

        
        average_list = []

        for row in students:
            total = 0
            grade_counter = 0
            for key,value in row.items():
                    if key != "Nombre completo" and key != "Sección":
                         grade = float(value)
                         total = total+grade
                         grade_counter = grade_counter+1
            average = total/grade_counter
            full_name = row["Nombre completo"]
            average_list.append((full_name,average))
        
        sorted_list = sorted(average_list, key=lambda x: x[1], reverse=True)
        
        for i, (name, average) in enumerate(sorted_list, start=1):
             print(f"{i}. {name} : {average:}")
        print("\n")

def delete_existing_student(file_path):
    name_to_search = input("Ingrese el nombre del estudiante que desea eliminar (Nombre y Apellido) : ").strip()
    rows = []
    students = data.import_all_students(file_path)
    exists = False
    status = "Unverified"

    
    for row in students:
         if row["Nombre completo"].strip().lower() == name_to_search.lower():
            print(f"Estudiante encontrado : {name_to_search}")
            exists = True
            choice = input(f"¿ Está seguro de que desea eliminar el estudiante {name_to_search} ? (Escriba SI para continuar) : ").strip().upper()
           
            if choice.upper() == "SI":
                status = "Verified"
                    

            else:
                    rows.append(row)
                    status = "Unverified"
         else:
              rows.append(row)
                
    if exists and status == "Verified":
        data.overwrite_all_students(file_path, rows)
        print(f"El estudiante '{name_to_search}' ha sido eliminado exitosamente.")
    elif not exists:
         print(f"Error: El estudiante '{name_to_search}' no existe en el registro. Asegúrese de escribir el nombre en formato Nombre + Apellido")
    else:
         print("Operación cancelada por el usuario.")


def view_failed_students(file_path):
    subjects = ["Nota de español", "Nota de inglés", "Nota de sociales", "Nota de ciencias"]
    found = False
    students = data.import_all_students(file_path)
    print("Lista de estudiantes con notas reprobadas, sección y materia de la nota : ")
    print("------------------------------------------------------------------------------")

    for row in students:
        failed_grades = []

        for s in subjects:
            if float(row[s]) <= 60:
                 failed_grades.append(f"{s}: {row[s]}")
        if failed_grades:
            found = True
            full_name = row["Nombre completo"]
            section = row["Sección"]
            details = " | ".join(failed_grades)


            print(f"{full_name:<25} : {section:<8} : {details}")
    print("\n")

    if not found:
         print("No se encontraron estudiantes con notas reprobadas.")