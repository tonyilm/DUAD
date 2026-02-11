global_variable = 100

def test_function():
    global global_variable
    if global_variable != 0:
        global_variable=global_variable+100
        print(f"El nuevo valor de la variable global es: {global_variable}")


test_function()

def test_function2():
    local_variable=50
    return local_variable


local_variable=test_function2()
print(f" El valor de la variable local es : {local_variable}")
