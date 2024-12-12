import time
with open("archivo_salida.txt", "w") as archivo:
    #Nombre del usuario
    archivo.write(nombre +'\n')
    #Fecha
    fecha_actual=time.localtime()
    dia =fecha_actual.tm_mday
    mes =fecha_actual.tm_mon
    year =fecha_actual.tm_year
    formato_de_fecha=f"{dia}/{mes}/{year}"
    archivo.write(f"La fecha en la que realizo esta partida es {formato_de_fecha}\n")
    # Escribir la matriz en un archivo de texto
    for fila in matriz:
        for elemento in fila:
            archivo.write(f"{elemento} ")
        archivo.write("\n")


    #Tablero en su estado final 

    #Movimientos y Puntos
    def calcular_puntaje(tablero):
        puntaje_total = 0
        for fila in tablero:
            for elemento in fila:
                puntaje_total += elemento
        return puntaje_total
    puntos=calcular_puntaje(tablero)
    archivo.write(f"Su cantidad de movimientos usados fueron {movimientosf}\n")
    archivo.write(f"Su cantidad de puntos generados fueron {puntos} \n")

def ganador(tablero):


    '''Devuelve True si se alcanza la cifra de 2048'''


    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 2048:
                print("Felicidades has ganado el juego , llegaste a los 2048 puntos")
                return True
    return False


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
#Estos if van dentro del main y van de ultimos
if ganador(tablero) and not mostrar_ganado:
        mostrar_ganado = True
        imprimir_tablero(tablero)
        print("-------- HAS GANADO --------")

if len(puede_moverse(tablero)) == 0 and sin_movimientos(tablero) == True:
        print("-------- HAS PERDIDO --------")
        print("-----------------------------")
        break