grade_counter=1
passing_grades_counter=0
failing_grades_counter=0
avg_passing_grades=0
avg_failing_grades=0
total_grade_avg=0
grade_total=int(input("Ingrese la cantidad de notas:"))
while grade_counter<=grade_total:
    current_grade=int(input(f"Ingrese la nota numero {grade_counter}:"))
    grade_counter=grade_counter+1
    if current_grade<70:
        failing_grades_counter=failing_grades_counter+1
        avg_failing_grades=avg_failing_grades+current_grade
    elif current_grade>=70:
        passing_grades_counter=passing_grades_counter+1
        avg_passing_grades=avg_passing_grades+current_grade
    total_grade_avg=total_grade_avg+(current_grade/grade_total)
avg_failing_grades=avg_failing_grades/failing_grades_counter if failing_grades_counter>0 else 0
avg_passing_grades=avg_passing_grades/passing_grades_counter if passing_grades_counter>0 else 0
print(f"El estudiante tiene esta cantidad de notas aprobadas:{passing_grades_counter}")
print(f"Este es el promedio de notas aprobadas: {avg_passing_grades}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas :{failing_grades_counter}")
print(f"Este es el promedio de notas desaprobadas: {avg_failing_grades}")
print(f"Este es el promedio total de notas: {total_grade_avg}")


    
