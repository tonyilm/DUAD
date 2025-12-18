def word_counter_function(path):
    with open(path, "r",encoding="utf-8") as file_in:
        text = file_in.read()
        words_only = len(text.split())
    
    
    print(f"Este archivo contiene : {words_only} palabras")





word_counter_function("dogs.txt")