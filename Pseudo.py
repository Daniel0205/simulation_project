
#Datos de la simulación
#Las variables contienen el rango dentro del cual se deben 
#generar los numeros siguiendo una distribucion uniforme
#LLEGADA_PIEZAS_ = [menor_valor, maximo_valor]
LLEGADA_PIEZASA = [5,7] 
LLEGADA_PIEZASB = [3,5]

SEMILLA = obtenerHoraActual() #Semilla generador
random(SEMILLA) #se inicializa el generador de numeros aleatorios
                #con la semilla del reloj


#Se definen las variables del sistema
COLA = []
PIEZASA_TORNEADAS = 0
PIEZASB_TORNEADAS = 0
TIEMPO_TRANSCURRIDO = 0
LIMITE_TIEMPO = 0
#PIEZASA_CREADAS = 0

#Definimos la funcion que simulará el comportamiento del generador
#de piezas del tipo A
generarPiezasA():
    ESPERAR LLEGADA_PIEZASA # sugiero que coloquemos PIEZASA_CREADAS+=1
        COLA.agregar(PiezaA) #se agrega una pieza de tipo B a la cola?
        LLEGADA_PIEZASA = random(5,7) #Se genera un numero aleatorio
        							  #para el tiempo de llegada

#Definimos la funcion que simulará el comportamiento del generador
#de piezas del tipo B
generarPiezasB():
    ESPERAR LLEGADA_PIEZASB
        COLA.agregar(PiezaB)
        LLEGADA_PIEZASB = random(3,5)

#En este bloque de codigo se inicializan las funciones definidas
#previamente y se crea un ciclo que solo terminará cuando el tiempo
#definido para la duracion de la simulación termine.
iniciarSimulacion():
    generarPiezasA()
    generarPiezasB()
    MIENTRAS (TIEMPO_TRANSCURRIDO<LIMITE_TIEMPO):
        SI (COLA.tamano()!=0):
            TIEMPO_TORNEADO=random(1,3) #Se genera un tiempo aleatorio de torneado
            tornear(COLA[0]) #Se tornea el primero de la cola de espera
            COLA[0].sacarDeLaCola() #Una vez se ha torneado la pieza actual, se
            						#quita de la cola de espera
            
            #se incrementa el tiempo transcurrido segun el evento que 
            #acabe de ocurrir, basado en, si hay elementos en la cola de espera
            TIEMPO_TRANSCURRIDO=TIEMPO_TRANSCURRIDO+TIEMPO_TORNEADO
        SI NO:
            TIEMPO_TRANSCURRIDO=TIEMPO_TRANSCURRIDO+minimo(LLEGADA_PIEZASA,LLEGADA_PIEZASB)
            #Se incrementa la cantidad de piezas torneadas por cada tipo
            SI nombre = 'Pieza B'
                        PIEZASB_TORNEADAS+= 1
                SI NO:
                        PIEZASA_TORNEADAS+=1

#Se llama al bloque de codigo, previamente definido, que inicializa la simulacion 
iniciarSimulacion():