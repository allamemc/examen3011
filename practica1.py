#En consola aparecen tres opciones
#1. historia
#2. matemáticas
#3. química
#el usuario debe elegir una opción.
#si la pregunta es historia, le pregunta qué animal mató a Cleopatra
#si la pregunta es matemáticas, le pregunta cuál es el seno de 90
#si lapregunta es química, le pregunta cuál es el símbolo químico del potasio
#muestra cuánto tiempo ha tardado en realizar el test
#sólo se hace una pregunta

import time
inicio=time.time()

def eleccion():
    print('1. historia\n2. matemáticas\n3. química')
    x= input('elija una opcion: ')
    #hacemos un match case para seleccionar una de las tres
    match x:
        case '1':
            #no necesitamos trycatch en caso de que ponga un numeor lo convierte a str y sale como incorrecto
            respuesta = input('qué animal mató a Cleopatra: ')
            respuestaslocas=['cobra','áspid','aspid']
            while respuesta.lower() not in respuestaslocas:
                print('Respuesta incorrecta')
                respuesta = input('qué animal mató a Cleopatra: ')
            print('Respuesta correcta')
        case '2':
            try:
                respuesta = int(input('cuál es el seno de 90: '))
                while respuesta != 1:
                    print('Respuesta incorrecta')
                    respuesta = int(input('cuál es el seno de 90: '))
                print('Respuesta correcta')
            except:
                print('Introduzca un numero')
        case '3':
            respuesta = input('cuál es el símbolo químico del potasio: ')
            while respuesta.upper() != 'K':
                print('Respuesta incorrecta')
                respuesta = input('cuál es el símbolo químico del potasio: ')
            print('Respuesta correcta')
        case _:
            print('Seleccione una opcion valida')
            eleccion()
eleccion()
fin=time.time().__round__()
print(f' Has tardado {fin-inicio.__round__()} segundos')