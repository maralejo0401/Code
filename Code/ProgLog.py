"""
@author: Marlon Hernández
Matera: Programación 
"""
import numpy as np


#--------------Definiendo variables--------------#
F1=15 #kN
F2=25 #kN
F3=20#KN


#-----------------Reacciones -------------------#
Ay=[]                      #reacciones en el eje x de la articulación 
Ax=0                       #reacciones en el eje y de la articulación[ÚNICA]. 
By=np.arange(1,100,0.5)    #reacción en el eje y del rodillo 

#----------------distancias--------------------#

d1=3*np.cos(60*np.pi/180) #metros [m]
d2=2                      #metros [m]
d3=2                      #metros [m]
d4=3                      #metros [m]


#=============================CONDICIONES DE EQUILIBRIO=====================#


#____________Encontrando las reacciones AY________________#
        

                    #SUMATORIA DE FUERZAS EN EL EJE Y
        
#-----------------># [Ay + By = 40 + 20]<-------------------------

#-------------------#sumatoria de torques RESPECTO AL PUNTO A#--------------#

# definir torques 
T1=F1*d1
T2=F2*(d1+d2)
T3=F3*(d1+d2+d3)
T4=By*d4

#_____________Torque en sentido Horario_______________________

SumTP=round((T1+T2+T3),3)

#_____________Torque en sentido antihorario___________________

SumTN=(T4)      #único Momento en sentido antiorario___-Torque de By

BYY=[] #se almacenan los valores posible que pueden tomar la reacción en By

#bucle para encontrar Reacciones By----------------

for i in range(len(T4)):
    By=np.arange(1,100,0.5)
    T4=(By*d4)                      #Momento de By
    TT4=T4[i]
    SumTP=round((T1+T2+T3),3)       #torque sentido  horario
    A=SumTP/TT4               #para que sea igual la divición será cercana a 1
    if A>1.01:                  #primera condición
        By == By+0.5
        
    elif A<0.99 :               #primera condición
        By == By-0.5
    else:  #solo pasarán los valores muy cercanos a 1, cuando los torque se igualan
        print("Uno de los valores de la reacción By podria ser",T4[i])
        BYY.append(T4[i])  #se agregan las reacciones By en la lista BYY
        #____________Encontrando las reacciones AY________________#
        #SUMATORIA DE FUERZAS EN EL EJE Y# [Ay + By = 40 + 20]
        Ay.append(60+T4[i])

print("valores posibles para By almacenados en una lista",BYY)
print("valores posibles para Ay almacenados una lista",Ay)

print("-------FIN----------")




    
    
        
   
