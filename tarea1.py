a=0
while a==0:
    while True:
     try:
        x=float(input("introduzca el primer numero:"))
        break
     except ValueError:
        print("Oops!  introduzca un valor numerico. Intente nuevamente...")
    
    while True:
     try:
        y=float(input("introduzca el segundo numero:"))
        break
     except ValueError:
        print("Oops!  introduzca un valor numerico. Intente nuevamente...")    
    
    while True:
     try:
        z=input("Que desea realizar?\n1-Suma\n2-Resta\n3-Multiplicasion\n4-Division\n5-Cualquier otro numero para salir\n")
        break
     except ValueError:
        print("Oops!  introduzca un valor numerico. Intente nuevamente...") 
    
    match z:
        case "1":
         suma= x+y
         print ("\n"+str(x) + "+" + str(y))
         print ("--------------------------------")
         print ("|El resultado de la suma es: " + str(suma) + "|")
         print ("--------------------------------\n") 

        case "2":
         resta= x-y
         print ("\n"+str(x) + "-" + str(y))
         print ("--------------------------------")
         print ("|El resultado de la resta es: " + str(resta) + "|")
         print ("--------------------------------\n")

        case "3":
         multiplicar = x*y
         print ("\n"+str(x) + "*" + str(y))
         print ("------------------------------------------")
         print ("|El resultado de la multiplicasion es: " + str(multiplicar) + "|")
         print ("------------------------------------------\n")

        case "4":
         dividir= x/y
         print ("\n"+str(x) + "/" + str(y))
         print ("-------------------------------------")    
         print ("|El resultado de la division es: " + str(dividir) + "|")
         print ("-------------------------------------\n")

        case _:
         print("\nERROR ---- opcion no valida!")
    
    while True:
     try:
        a=int(input("\nDesea realizar otra consulta? \n Si - 0\n No - cualquier otro numero\n"))
        break
     except ValueError:
        print("Oops!  introduzca un valor numerico. Intente nuevamente...")
print("Gracias por usar este script!!!!!")