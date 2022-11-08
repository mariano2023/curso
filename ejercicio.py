
import datetime #se importa la libraria tiempo de Python 
ahora= datetime.datetime.now() # se define la variable "ahora" con la fecha y hora completa, inclusive ms
times=ahora.strftime('%H:%M:%S') # se define la variable "times" con la fecha y hora completa, sin ms
tasks= [] #se define la lista "task"
aux=0 # se define la variable "aux" con el valor 0
count=int(input("La cantidad de eventos que quiero agendar : ")) #se define una cantidad de ciclos
file=open("tareas2.txt", "w", encoding="utf_8") #se abre y escribe el archivo "tareas.txt"
print("Software To_Do V1.0")
for _ in range(count): # se define el bucle for con la variable auxiliar " _ ", 
    aux=aux+1       # es un contador de aux, suma 1 en cada ciclo
    element_1=(input("Definir actividad : ")) # la variable "element_1" contiene la tarea a definir en cada ciclo
    element_2=(input("Ingresar prioridad R, A, V: ")) # la variable "element_2" contiene la prioridad a definir en cada ciclo
    tasks.append(aux) # se agrega el ID en la lista "task"
    tasks.append(element_1) #se guarda la respuesta en la lista "task"
    #tasks.append(times) #se agrega a la lista "task" la fecha y hora actual de cada tarea
    file.write(str(aux) + " | " + element_1) # + " | " + str(times)) #write es un metodo, se guarda la info de la lista
    file.write('\n') #con esto se logra que este uno debajo de otro
print(tasks) 
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))

file.close() 


