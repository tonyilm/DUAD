def read_and_write_text(path,output_path):
    lines = []
    with open(path, "r",encoding="utf-8") as file_in:
          for line in file_in:
                print(line)
                lines.append(line)


                
      
    with open(output_path,"w",encoding="utf-8") as file_out:
         for line in lines:
              line = line.rstrip()
              file_out.write(line + " ")
      
        
        
    
            
            
read_and_write_text("my_text_file.txt","my_new_text_file.txt")

    