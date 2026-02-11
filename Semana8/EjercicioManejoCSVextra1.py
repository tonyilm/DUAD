import csv

def csv_reader(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)


        for row in reader:
            for i in range(len(headers)):
                print(f"{headers[i]}: {row[i]} \n ---------------------------------")
              
            


csv_reader("videogames.csv")