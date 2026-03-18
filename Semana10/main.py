import menu
import actions




def main():
    file_path = "student_file.csv"
    temp_student_list = []
    while True:
        operation = menu.initial_menu()
        if operation == "1":
            actions.add_new_student(temp_student_list)
        elif operation == "2":
            actions.view_existing_student(temp_student_list)
        elif operation == "3":
            actions.view_top_three(temp_student_list)
        elif operation == "4":
            actions.view_student_average(temp_student_list)
        elif operation == "5":
            actions.delete_existing_student(temp_student_list)
        elif operation == "6":
            actions.view_failed_students(temp_student_list)
        elif operation == "7":
            actions.export_to_csv(temp_student_list,file_path)
        elif operation == "8":
            actions.import_from_csv(temp_student_list,file_path)
        elif operation == "9":
            print("Saliendo del sistema :D\n")
            break
        else:
            print("Opción no válida, intente de nuevo")



if __name__ == "__main__":
    main()