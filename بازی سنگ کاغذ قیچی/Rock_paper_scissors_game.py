import random
print("\n ----------------- \n Hellps : S = Sang , G = Gheychi , K = Kaghaz \n ----------------- \n")
L = ['S', 'K', 'G']

Score1 = Score2 = 0 
i = 3 
while True :
    
    print("\n--- Hello, Welcome To The Game --- \n \n Menu { \n \t 1- Start the game \n \t 2- Number of rounds in the game \n \t 3- Exite \n } \n")
    I = int(input("\nEnter a number : "))
    
    if I != '' :
        if I == 1 :
        
            for s in range(i) : 
                A = input("\n which one (S , G , K) : ")
                B = random.choice(L)
                print ("\n \t Camputer : ", B)
            #----------------win camputer-------------------
                if A == 'S' or A == 's' and B == 'K':
                    Score2 = Score2 + 1 
                if A == 'G' or A == 'g' and B == 'S':
                    Score2 = Score2 + 1 
                if A == 'K' or A == 'k' and B == 'G':
                    Score2 = Score2 + 1
            #----------------win user-------------------
                if A == 'K' or A == 'k' and B == 'S':
                    Score1 = Score1 + 1 
                if A == 'S' or A == 's' and B == 'G':
                    Score1 = Score1 + 1 
                if A == 'G' or A == 'g' and B == 'K':
                    Score1 = Score1 + 1
            #------------end for-----------------------
            if Score1 > Score2 :
                print (f"\n Your score {Score1} \n Camputer score {Score2} \n")
                print ("-- ! You Win The GAME ! --")
            else :
                print (f"\n Your score : {Score1} \n Camputer score : {Score2} \n")
                print ("-- ! You Lost ! --")
        #---------------------end if-------------------------------------
    
        if I == 2 :
            print ("Number of game rounds : ", i)
            i = int(input("Enter a number to change (3 , 11) : "))
        if I == 3 :
            exit()
    else :
        I = int(input("\n Enter a number : "))