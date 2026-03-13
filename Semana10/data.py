import csv
import os

def export_students_to_csv(file_path, student_list, headers):
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerows(student_list)

def import_all_students(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader) 
    except FileNotFoundError:
        return []

def overwrite_all_students(file_path, student_list):
    if not student_list:
        return 
    headers = list(student_list[0].keys())
    
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(student_list)