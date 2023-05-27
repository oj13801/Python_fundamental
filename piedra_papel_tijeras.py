#piedra, papel y tijeras. 
import random
print("Bienvenido a Piedra, papel o tijera !!!")
x=0 #variable usada para no salir del ciclo
#Iniciamos los contadores del marcador
Gane=0
Empate=0
Perdidas=0
#Iniciamos el ciclo mientras x sea igual a 0 
while x==0:
    Jugador=input("introdusca una de las siguientes opciones:  \nPiedra \nPapel \nTijera\n")#entrada por teclado del usuario
    Opciones=["Piedra","Papel","Tijera"] #lista con las opciones del CPU
    CPU=random.choice(Opciones) # Selecciona aleatoriamente un elemento de la lista 
    if Jugador==CPU:
        print("!!Es un Empate El jugador escojio: " + Jugador + " La Maquina escojio: " + CPU )
        Empate=Empate+1
    else:
        match Jugador:
            case "Piedra":
                if CPU=="Papel":
                    print("Has perdido El jugador escojio: " + Jugador + " La Maquina escojio: " + CPU)
                    Perdidas=Perdidas+1
                else :
                    print("Has Ganado!!!!! El jugador escojio: " + Jugador + " La Maquina escojio: " + CPU) 
                    Gane=Gane+1

            case "Papel":
                if CPU=="Tijera":
                    print("Has perdido El jugador escojio: " + Jugador + " La Maquina escojio: " + CPU)
                    Perdidas=Perdidas+1
                else :
                    print("Has Ganado!!!!! El jugador escojio: " + Jugador + " La Maquina escojio: " + CPU)
                    Gane=Gane+1

            case "Tijera":        
                if CPU=="Piedra":
                    print("Has perdido El jugador escojio: " + Jugador + " La Maquina escojio: " + CPU)
                    Perdidas=Perdidas+1
                else :
                    print("Has Ganado!!!!! El jugador escojio: " + Jugador + "La Maquina escojio: " + CPU)
                    Gane=Gane+1

            case _:
                print("\nERROR ---- opcion no valida!") #desplega un error si el usuario introduce otra opcion por medio del teclado 

    print("Asi va el marcador: \nGanados:" + str(Gane) + "\nEmpatados: " + str(Empate) + "\nPerdidos: " + str(Perdidas))   #muestra el marcador luego de la ronda         
    try:
        x=int(input("Desea seguir Jugando? 0 - SI Cualquier otro numero - NO  \n****El Juego se Finalizara si no introduce un valor numerico del 0 al 9****\n"))
    except ValueError:
        print("Oops!  introduzca un valor numerico. Intente nuevamente...")   #despliega un error y acaba el juego si no se selecciona un valor numerico
        break
print("Gracias por jugar!! :) ")