def vowel_function() :
    string = input("Ingrese el texto : ")
    vowels = "aeiou"
    vowel_counter = 0
    for letter in string.lower():
        if letter in vowels:
            vowel_counter = vowel_counter+1
    print(vowel_counter)
    

vowel_function()


