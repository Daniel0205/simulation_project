
#Datos de la simulación
LLEGADA_PIEZASA = 0
LLEGADA_PIEZASB = 0

SEMILLA = obtenerHoraActual() #Semilla generador
random(SEMILLA) #se inicializa el generador de numeros aleatorios
                #con la semilla del reloj


#Se definen las variables del sistema
COLA = []
PIEZASA_TORNEADAS = 0
PIEZASB_TORNEADAS = 0
TIEMPO_TRANSCURRIDO = 0
LIMITE_TIEMPO = 0


generarPiezasA():
    ESPERAR LLEGADA_PIEZASB
        COLA.agregar(PiezaB)
        LLEGADA_PIEZASA = random(5,7)

generarPiezasB():
    ESPERAR LLEGADA_PIEZASA
        COLA.agregar(PiezaA)
        LLEGADA_PIEZASA = random(3,5)


iniciarSimulacion():
    generarPiezasA()
    generarPiezasB()
    MIENTRAS (TIEMPO_TRANSCURRIDO<LIMITE_TIEMPO):
        SI (COLA.tamano()!=0):
            TIEMPO_TORNEADO=random(1,3)
            tornear(COLA[0])
            COLA[0].sacarDeLaCola()
            
            TIEMPO_TRANSCURRIDO=TIEMPO_TRANSCURRIDO+TIEMPO_TORNEADO
        SI NO:
            TIEMPO_TRANSCURRIDO=TIEMPO_TRANSCURRIDO+minimo(LLEGADA_PIEZASA,LLEGADA_PIEZASB)


iniciarSimulacion():