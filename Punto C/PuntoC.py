# -*- coding: utf-8 -*-
#Instalar https://simpy.readthedocs.io/en/latest/simpy_intro/installation.html
#Ejemplos https://simpy.readthedocs.io/en/latest/examples/index.html
import random
import simpy
import numpy
from datetime import datetime

#Datos de la simulación
SEMILLA = datetime.now() #Semilla generador
LIMITE_PIEZAS = 314 #Vamos a simular 10 clientes
LLEGADA_PIEZASA = [5, 7] #Clientes llegan cada 10 segundos en una distribución uniforme
LLEGADA_PIEZASB = [3, 5] #Clientes llegan cada 10 segundos en una distribución uniforme
TIEMPO_TORNEADO = [1,3] #Clientes son atendidos en una distribucion


#Variables desempeño
COLA = 0
MAX_COLA = 0
ESPERA_CLIENTES = numpy.array([])
PIEZASA_TORNEADAS = 0
PIEZASB_TORNEADAS = 0

def llegadaA(env,  contador):
    j=0
    while  PIEZASA_TORNEADAS+PIEZASB_TORNEADAS<LIMITE_PIEZAS-1:  
                c = torneado(env, 'Pieza A  %02d' % j, contador)
                env.process(c)
                tiempo_llegada = random.uniform(LLEGADA_PIEZASA[0],LLEGADA_PIEZASA[1])
                print("AAAAAAA-%02d:" % (j+1) ,tiempo_llegada)
                yield env.timeout(tiempo_llegada) #Yield retorna un objeto iterable
                j+=1
                


def llegadaB(env, contador):
    i=0
    while  PIEZASA_TORNEADAS+PIEZASB_TORNEADAS<LIMITE_PIEZAS:                
                c = torneado(env, 'Pieza B %02d' % i, contador)
                env.process(c)
                tiempo_llegada = random.uniform(LLEGADA_PIEZASB[0],LLEGADA_PIEZASB[1])
                print("BBBBBBB-%02d:" % (i+1) ,tiempo_llegada)
                yield env.timeout(tiempo_llegada) #Yield retorna un objeto iterable
                i+=1
                
        
        
def torneado(env, nombre, servidor):
    #El cliente llega y se va cuando es atendido
    llegada = env.now
    print('%7.2f'%(env.now)," Llega la ", nombre)
    global COLA
    global MAX_COLA 
    global ESPERA_CLIENTES   
    global PIEZASB_TORNEADAS
    global PIEZASA_TORNEADAS

    #Atendemos a los clientes (retorno del yield)
    #With ejecuta un iterador sin importar si hay excepciones o no
    with servidor.request() as req:
		
		#Hacemos la espera hasta que sea atendido el cliente
                COLA += 1
                if COLA > MAX_COLA:
                        MAX_COLA = COLA
		
                #print("Tamaño cola", COLA)
                results = yield req	
                COLA = COLA - 1
                espera = env.now - llegada
                ESPERA_CLIENTES = numpy.append(ESPERA_CLIENTES, espera)

                print('%7.2f'%(env.now), " La  ",nombre," espera a ser torneada ",espera)

                tiempo_atencion = random.uniform(TIEMPO_TORNEADO[0],TIEMPO_TORNEADO[1])
                print("ATENCIONNNNNNNNNN ",tiempo_atencion)
                yield env.timeout(tiempo_atencion)
                if(nombre.find('Pieza B')!=-1):
                        PIEZASB_TORNEADAS+= 1
                else:
                        PIEZASA_TORNEADAS+=1

                print('%7.2f'%(env.now), " Sale la pieza ",nombre)

                    
#Inicio de la simulación

print('Departamento de torneado')
random.seed(SEMILLA)
env = simpy.Environment()

#Inicio del proceso y ejecución
torno = simpy.Resource(env, capacity=1)
env.process(llegadaA(env, torno))
env.process(llegadaB(env, torno))
env.run()

print("Cola máxima ",MAX_COLA)
print("Piezas A torneadas: ",PIEZASA_TORNEADAS)
print("Piezas B torneadas: ",PIEZASB_TORNEADAS)
print("Tiempo promedio de espera ",'%7.2f'%(numpy.mean(ESPERA_CLIENTES)))
