keys_to_delete = ["age","surname"]
employee_data = {
    "name": "Robert",
    "email": "robertfinn@treehouse.com",
    "age": 20,
    "surname": "Finn"
}

for key in keys_to_delete:
    employee_data.pop(key)


print(employee_data)