Dic= {"Saturday" : 0 ,"Sunday" : 1 ,"Monday" : 2 ,"Tuesday" : 3 ,"Wednesday " : 4 ,"Thursday " : 5 ,"Friday" : 6}
print ("Hellp : Saturday , Sunday , Monday , Tuesday , Wednesday , Thursday , Friday ")
while True :
    
    I = input(" Enter one of the days of the week : ")

    if I != "":
        print("\n \t", Dic[I])
    elif I == 'exit' or I == 'Exit' :
        exit()
    