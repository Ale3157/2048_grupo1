#Importaciones
#import os
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
# Función para colocar un número aleatorio (2 o 4) en una posición vacía
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
    
def puede_moverse(tablero):
    #Comprobamos que las casillas esten vacias 
    vacias = []
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 0:
                vacias.append([i,j])
    return vacias

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

###########################################################



vacias = puede_moverse(tablero)

tablero = colocar_numero(tablero, vacias)
movimientos = 1

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

def main():
    #Se crea el tablero 4x4
    tablero=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
            ]

    while True:
        #os.system("cls") #cAMBIAR
        if movimientos != 0:
            vacias = puede_moverse(tablero)
            tablero = colocar_numero(tablero, vacias)

        jugada = ""

        while jugada not in ("a", "w", "s", "d","p"):
            #os.system("cls")
            #Mostrar el Tablero 4x4
            print("**Bienvenido al tablero maldito.")
            imprimir_tablero(tablero) #Se llama la función imprimir tablero y se muestra por pantalla
            jugada = input(" Utiliza (w/a/s/d) para moverte, Presiona P/p  para salir -> ")

        else:
            #Movimientos en Tablero
            if jugada == "w": #Arriba
                tablero, movimientos = mover_arriba(tablero)


            elif jugada == "s": #Abajo
                tablero, movimientos = mover_abajo(tablero)


            elif jugada == "d": #Derecha
                tablero, movimientos = mover_derecha(tablero)


            elif jugada == "a": #Izquierda
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
                    break
            

if __name__ == "__main__":
    main()