list_a = ["Name","Release year","Artist"]
list_b = ["White Pony",2000,"Deftones"]
my_dictionary = {}
if len(list_a) == len(list_b):
        for element in range(len(list_a)):
            my_dictionary[list_a[element]]=list_b[element]
print(my_dictionary)