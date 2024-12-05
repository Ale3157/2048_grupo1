import time
with open("archivo_salida.txt", "w") as archivo:
    #Nombre del usuario
    nombre_del_usuario="Alejandro"
    archivo.write(nombre_del_usuario +'\n')
    #Fecha
    fecha_actual=time.localtime()
    dia =fecha_actual.tm_mday
    mes =fecha_actual.tm_mon
    year =fecha_actual.tm_year
    formato_de_fecha=f"{dia}/{mes}/{year}"
    archivo.write(f"La fecha en la que realizo esta partida es {formato_de_fecha}\n")

    #Tablero en su estado final 

    #Movimientos y Puntos
    movimientos=10
    puntos=100
    archivo.write(f"Su cantidad de movimientos usados fueron {movimientos}\n")
    archivo.write(f"Su cantidad de puntos generados fueron {puntos} \n")