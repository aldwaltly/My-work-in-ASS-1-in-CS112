while True :
    while True:
        result=''
        print("***************************************************************")
        print("A)Find the factors of +ve integer")
        print("B)Exit")
        choise1=input("Please choose option: ")
        if choise1 not in ['A','a','B','b']:
            print("Plesae insert valid choise")
            continue
        else: break
    if choise1 == "B"or choise1=="b":break
    else:
        while True:
           number=int(input("Please enter the number: "))
           if number <=0:
               print("Please insert a +ve and not equal 0 number")
               continue
           else:
               break
        for i in range (1,number+1):
            if number%i==0:
                result+=str(i)+" "
        print("The factors of this number is: ")
        print(result)