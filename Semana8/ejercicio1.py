def read_and_write_songs(path,outputh_path):
    lines = []
    with open(path, "r",encoding="utf-8") as file_in:
          for line in file_in:
                line = line.rstrip()
                print(line)
                lines.append(line)
    lines.sort()  
        
        
        
    with open(outputh_path,"w",encoding="utf-8") as file_out:
         for line in lines:
              file_out.write(line + "\n")
            
            
            


read_and_write_songs("songs.txt","songs_sorted.txt")

    