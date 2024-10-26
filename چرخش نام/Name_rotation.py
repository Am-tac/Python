# تعریف یک تابع
def Potate(s,n) :
    return s[-n:] + s[:len(s) - n]

while True :
    Name = input(" Enter Your Name : ")
    Num = int(input(" enter numbere : "))

    print(Potate(Name , Num))
    