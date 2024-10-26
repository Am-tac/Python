while True :
    print("ــــــــــــــــ calculator ــــــــــــــــ ")
    print("ــــــــــــــــــــــــــــــــــــــــــــ")
    X= input(" -- Enter the first number : ")
    Y= input(" -- Enter the second number : ")
    print("ــــــــــــــــــــــــــــــــــــــــــــ")
    
    while X != '' and Y != '' :
        
        if X != '' and Y != '':
            x = float(X)
            y = float(Y)
            print("ــــــــــــــــــــــــــــــــــــــــــــ")
            print(" -- Enter one of the numbers : ")
            Z = input(" -- 1(+) 2(-) 3(/) 4(*) 5(**) 6(%) 7(//)  e(exit) s(Choose numbers again) -- :  ") 
            print("ــــــــــــــــــــــــــــــــــــــــــــ")           
            if Z != '' :
                match Z :
                    case  '1' :
                        A = x + y
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        print (" -- The sum of these ", x , " With this number ", y , " is equal to: " , A)
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                    case "2" :
                        A = x - y
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        print (" -- The result of subtracting this number ", x , " With this number ", y , " is equal to: " , A)
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                    case "4" :
                        A = x * y
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        print (" -- The product of this number ", x , "With this number ", y , " is equal to: " , A)
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                    case "3" :
                        A = x / y
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        print (" -- The result of dividing this number ", x , "With this number ", y , " is equal to: " , A)
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                    case "5" :
                        A = x ** y
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        print (" -- The result can be this number ", x , "With this number ", y , " is equal to: " , A) 
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                    case "6" :
                        A = x % y
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        print (" -- The remainder of this number ", x , "With this number ", y , " is equal to: " , A)
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                    case "7" :
                        A = x ** 0.5
                        B = y ** 0.5
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        print (" -- root of a number ", x ," : ", A)
                        print (" -- root of a number ", y ," : ", B)
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                    case 'e' :
                        exit()
                    case 's' :
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        X= input(" -- Enter the first number : ")
                        Y= input(" -- Enter the second number : ")
                        print("ــــــــــــــــــــــــــــــــــــــــــــ")
                        
            else : 
                print("ــــــــــــــــــــــــــــــــــــــــــــ")
                print(" -- Enter a number...!")
                Z = input(" -- 1(+) 2(-) 3(/) 4(*) 5(**) 6(%) 7(//)  0(exit) s(Choose numbers again) -- :  ")
                print("ــــــــــــــــــــــــــــــــــــــــــــ")
        else :
            print("ــــــــــــــــــــــــــــــــــــــــــــ")
            print(" -- Enter a number")
            X= input(" -- Enter the first number : ")
            Y= input(" -- Enter the second number : ")
            print("ــــــــــــــــــــــــــــــــــــــــــــ")
        
    
    
        
                
                
            
    
    

