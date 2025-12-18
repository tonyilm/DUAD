def uppercase_text_function(path,output_path):
    with open(path,"r" ,encoding = "utf-8") as file_in:
        text = file_in.read()
        
        

    

    with open(output_path,"w" ,encoding = "utf-8") as file_out:
        file_out.write(text.upper())




uppercase_text_function("deftones.txt", "uppercase.txt")

