def uplow_function() :
    my_string = "I live in Chicago, Illinois"
    uppercase = 0
    lowercase = 0
    for char in my_string:
        if char.isupper():
            uppercase = uppercase+1
        elif char.islower():
            lowercase = lowercase+1
    print(f"There are {uppercase} upper cases and {lowercase} lower cases in this string")




uplow_function()

