#Importaciones
import os #Se utiliza para limpiar el tablero
import random #Usamos random para generar elementos aleatorios en el arreglo
import time #Usamos time para darle espera a ciertas acciones

#trasfondo del juego 
print("**2048: El tablero de las sombras eternas, cada movimiento convoca entidades oscuras**")
print("*Funde números iguales y libera energías siniestras.")
print("*Sobrevive, las sombras te observan.")
print("*Alcanza 2048 antes de que el vacío te consuma por completo.")

#Solicitar el nombre del jugador
print(" ") #Espacio en blanco
print("*Bienvenido a las sombras de 2048... Para comenzar, necesitamos tu nombre, valiente alma condenada...") #Mensaje Binvenida
nombre=str(input("*Ingrese su nombre viajero: ")) #Pedimos por pantalla el nombre
print(f"Bienvenido {nombre}... El juego comienza") #Se imprime un mensaje con el nombre escrito



#Generacion de un 4x4 con 2 numeros al azar, funcion generar tablero
# Función para colocar un número aleatorio (2) en una posición vacía
def colocar_numero(tablero,vacias):
    
    n = random.choice([2,2,2,2,2,2,2,2,2,4])

    casilla = random.choice(vacias)
    tablero[casilla[0]][casilla[1]] = n


    return tablero



#Funcion impresión del tablero
def imprimir_tablero(tablero):

  for fila in tablero:
    for elemento in fila:
      if(elemento == 0):
        print(f" |   ", end="") #Imprimir |elemento|
      else:
         print(f" | {elemento} ", end="") #Imprimir |elemento|
    print(" |")
    print("----------------------")

#Final de la primera parte
#***********************************************************
#***********************************************************
#***********************************************************


#Inicio de la segunda parte 
#Funcion para confirmar si se puede realizar un movimiento
def puede_moverse(tablero):
    #Comprobamos que las casillas esten vacias 
    vacias = []
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 0:
                vacias.append([i,j])
    return vacias

#Funcion movimiento a la Derecha 
def mover_derecha(t):


    '''Mueve las casillas a la derecha y realiza las mezclas'''


    mov = 0
    for y in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for x in range(-2, -len(t)-1, -1):
                if t[y][x] != 0 and t[y][x+1] == 0:
                    t[y][x+1] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y][x+1] and \
                     x not in mezclas and x-1 not in mezclas:
                    t[y][x+1] *= 2
                    t[y][x] = 0
                    mezclas.append(x)
                    mov += 1
    return t, mov



#Funcion movimiento a la Izquierda
def mover_izquierda(t):


    '''Mueve las casillas a la izquierda y realiza las mezclas'''


    mov = 0
    for y in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for x in range(1, len(t)):
                if t[y][x] != 0 and t[y][x-1] == 0:
                    t[y][x-1] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y][x-1] and \
                     x not in mezclas and x+1 not in mezclas:
                    t[y][x-1] *= 2
                    t[y][x] = 0
                    mezclas.append(x)
                    mov += 1
    return t, mov



#Funcion movimiento para Abajo
def mover_abajo(t):


    '''Mueve las casillas hacia abajo y realiza las mezclas'''


    mov = 0
    for x in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for y in range(-2, -len(t)-1, -1):
                if t[y][x] != 0 and t[y+1][x] == 0:
                    t[y+1][x] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y+1][x] and \
                     y not in mezclas and y-1 not in mezclas:
                    t[y+1][x] *= 2
                    t[y][x] = 0
                    mezclas.append(y)
                    mov += 1
    return t, mov



#Funcion movimiento para Arriba
def mover_arriba(t):


    '''Mueve las casillas hacia arriba y realiza las mezclas'''


    mov = 0
    for x in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for y in range(1, len(t)):
                if t[y][x] != 0 and t[y-1][x] == 0:
                    t[y-1][x] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y-1][x] and \
                     y not in mezclas and y+1 not in mezclas:
                    t[y-1][x] *= 2
                    t[y][x] = 0
                    mezclas.append(y)
                    mov += 1
    return t, mov

#Funcion tablero ganador(se llega a 2048)
def ganador(tablero):


    '''Devuelve True si se alcanza la cifra de 2048'''


    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 2048:
                print("Felicidades has ganado el juego , llegaste a los 2048 puntos")
                return True
    return False

#Funcion sin movimientos(el jugador no se puede mover mas)
def sin_movimientos(tablero):


    ''' Recorre el tablero y comprueba si no hay más movimientos'''


    final = True


    for y in range(len(tablero)):
        for x in range(len(tablero)-1):
            if tablero[y][x] == tablero[y][x+1]:
                final = False


    for y in range(len(tablero)-1):
        for x in range(len(tablero)):
            if tablero[y][x] == tablero[y+1][x]:
                final = False
    return final
###########################################################

#Funcion calcular puntaje 
def calcular_puntaje(tablero):
    puntaje_total = 0
    for fila in tablero:
        for elemento in fila:
            puntaje_total += elemento
    return puntaje_total

#Función principal(main)
def main():
    #Se crea el tablero 4x4
    tablero=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
            ]
    
    vacias = puede_moverse(tablero)

    tablero = colocar_numero(tablero, vacias)
    movimientos = 1
    movimientosT = 0
    mostrar_ganado = False

    #Mostrar el Tablero(Maztriz4x4)
    print(" ") #Espacio en blanco
    print("Prepárate... En 3 escalofriantes segundos, tu tablero se materializará desde las sombras...") #Mensaje terror
    time.sleep(1) #1 segundo
    print("1............................") #Mostrar 1.....
    time.sleep(1) #2 segundo
    print("2............................") #Mostrar 2.....
    time.sleep(1) #3 segundo, muestra tablero
    print("El tablero maldito se ha revelado. ¡Prepárate para lo desconocido!") #Mostramos mensaje y tablero
    print(" ") #Espacio en blanco

    while True:
        os.system("cls") 
        if movimientos != 0:
            vacias = puede_moverse(tablero)
            tablero = colocar_numero(tablero, vacias)

        jugada = ""

        while jugada not in ("a", "w", "s", "d","p"):
            os.system("cls")
            #Mostrar el Tablero 4x4
            print("**Bienvenido al tablero maldito.")
            imprimir_tablero(tablero) #Se llama la función imprimir tablero y se muestra por pantalla
            jugada = input(" Utiliza (w/a/s/d) para moverte, Presiona P/p  para salir -> ")

        else:
            #Movimientos en Tablero
            if jugada == "w": #Arriba
                movimientosT = movimientosT + 1
                tablero, movimientos = mover_arriba(tablero)


            elif jugada == "s": #Abajo
                movimientosT = movimientosT + 1
                tablero, movimientos = mover_abajo(tablero)


            elif jugada == "d": #Derecha
                movimientosT = movimientosT + 1
                tablero, movimientos = mover_derecha(tablero)


            elif jugada == "a": #Izquierda
                movimientosT = movimientosT + 1
                tablero, movimientos = mover_izquierda(tablero)
            
            elif jugada== "p" or "P": #Salir
                print("Usted escogió la opción de salir de la partida")
                opcion=input("Desea salir s(si) n(no)")
                if opcion=="s":
                    print("Usted va a salir en 3")
                    time.sleep(1) #1 segundo
                    print("2............................")
                    time.sleep(1) #2 segundo
                    print("1............................")
                    #Escribir en el archivo
                    with open("archivo_salida.txt", "w") as archivo:
                    #Archivo de salida(escritura) 
                        #Nombre
                        archivo.write(nombre +'\n')
                        #Fecha
                        fecha_actual=time.localtime()
                        dia =fecha_actual.tm_mday
                        mes =fecha_actual.tm_mon
                        year =fecha_actual.tm_year
                        formato_de_fecha=f"{dia}/{mes}/{year}"
                        #Puntaje
                        puntos=calcular_puntaje(tablero)
                        # Escribir el tablero en un archivo de texto
                        for fila in tablero:
                            for i, elemento in enumerate(fila):
                                archivo.write(f" {elemento} ")
                                if i < len(fila) - 1:
                                    archivo.write("|")
                            archivo.write("\n" + "-" * (len(fila) * 4 - 1) + "\n")
                        archivo.write(f"La fecha en la que realizo esta partida es {formato_de_fecha}\n")
                        archivo.write(f"Su cantidad de movimientos usados fueron {movimientosT}\n")
                        archivo.write(f"Su cantidad de puntos generados fueron {puntos} \n")
                        #Archivo de salida(lectura)
                    with open("archivo_salida.txt", "r") as archivo:
                        contenido = archivo.read()
                        print(contenido)
                    break
                
        if ganador(tablero) and not mostrar_ganado: #Si ganó
            mostrar_ganado = True
            imprimir_tablero(tablero)
            with open("archivo_salida.txt", "w") as archivo:
                #Archivo de salida(escritura)  
                archivo.write(nombre +'\n')
                #Fecha
                fecha_actual=time.localtime()
                dia =fecha_actual.tm_mday
                mes =fecha_actual.tm_mon
                year =fecha_actual.tm_year
                formato_de_fecha=f"{dia}/{mes}/{year}"
                puntos=calcular_puntaje(tablero)
                # Escribir el tablero en un archivo de texto
                for fila in tablero:
                    for i, elemento in enumerate(fila):
                        archivo.write(f" {elemento} ")
                        if i < len(fila) - 1:
                            archivo.write("|")
                    archivo.write("\n" + "-" * (len(fila) * 4 - 1) + "\n")
                archivo.write(f"La fecha en la que realizo esta partida es {formato_de_fecha}\n")
                archivo.write(f"Su cantidad de movimientos usados fueron {movimientosT}\n")
                archivo.write(f"Su cantidad de puntos generados fueron {puntos} \n")
            print("-------- HAS GANADO --------")
            with open("archivo_salida.txt", "r") as archivo: #Archivo de salida(lectura) 
                        contenido = archivo.read()
                        print(contenido)

        #Si no existen movimientos
        if len(puede_moverse(tablero)) == 0 and sin_movimientos(tablero) == True:
            with open("archivo_salida.txt", "w") as archivo: #Archivo de salida(escritura) 
                #Archivo de salida 
                archivo.write(nombre +'\n')
                #Fecha
                fecha_actual=time.localtime()
                dia =fecha_actual.tm_mday
                mes =fecha_actual.tm_mon
                year =fecha_actual.tm_year
                formato_de_fecha=f"{dia}/{mes}/{year}"
                puntos=calcular_puntaje(tablero)
                # Escribir el tablero en un archivo de texto
                for fila in tablero:
                    for i, elemento in enumerate(fila):
                        archivo.write(f" {elemento} ")
                        if i < len(fila) - 1:
                            archivo.write("|")
                    archivo.write("\n" + "-" * (len(fila) * 4 - 1) + "\n")
                archivo.write(f"La fecha en la que realizo esta partida es {formato_de_fecha}\n")
                archivo.write(f"Su cantidad de movimientos usados fueron {movimientosT}\n")
                archivo.write(f"Su cantidad de puntos generados fueron {puntos} \n")
            print("-------- HAS PERDIDO --------")
            print("-----------------------------")
            with open("archivo_salida.txt", "r") as archivo: #Archivo de salida(lectura) 
                contenido = archivo.read()
                print(contenido)
            break
            

if __name__ == "__main__":
    main()