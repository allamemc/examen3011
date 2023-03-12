#actividad1
#Solicita por consola la respuesta a una pregunta.
#El usuario puede responder hasta que acierte.
#Muestra los intentos que ha necesitado
# total 5 puntos.
#la aplicación funciona correctamente : 1 punto
#muestra la fecha y hora de inicio del test y fecha y hora de fin test : 1 punto
#control de errores y validación 1 punto
#la respuesta está en un array 1 punto
#la respuesta está en un archivo txt externo 1 punto

from datetime import *

def actividad1():
    x = ''
    y = 0
    #con datetime.now podemos sacar fecha y hora actual y cambiamos el formato a solo la hora minuto y segundo
    fecha_inicio=datetime.now()
    fecha_inicio_format= fecha_inicio.strftime('%H:%M:%S')
    print(f'INICIO TEST {fecha_inicio_format}')
    #respuesta en archivo txt
    leer_archivo = open("ciudad.txt", "r")
    archivo = leer_archivo.read()
    #respuesta dentro de lista
    lista_ciu=['paris','lisboa','madrid','berlin']  # lista de ciudades de donde recogemos el elemnto 2
    #el lower de x es la validacion del ejercicio
    while x.lower() != archivo:  # lista_ciu[2]  # 'madrid' para la aplicacion inicial
        y += 1 # incrementamos el valor de y en 1
        x = input('DIME LA CAPITAL DE ESPAÑA: ')

    print(f'NUMER DE INTENTOS = {y}')
    fecha_fin = datetime.now()
    fecha_fin_format = fecha_fin.strftime('%H:%M:%S')
    print(f'FIN TEST {fecha_fin_format}')
actividad1()
