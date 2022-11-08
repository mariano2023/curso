



tasks= [] #se define la lista "task"
aux=0 # se define la variable "aux" con el valor 0
count=int(input("La cantidad de eventos que quiero agendar : ")) #se define una cantidad de ciclos
file=open("tareas3.txt", "w", encoding="utf_8") #se abre y escribe el archivo "tareas.txt"
priority="vacia"
print("Software To_Do V1.0")
for _ in range(count): # se define el bucle for con la variable auxiliar " _ ", 
    aux=aux+1       # es un contador de aux, suma 1 en cada ciclo
    element_1=(input("Definir actividad : ")) # la variable "element_1" contiene la tarea a definir en cada ciclo
    element_2=int(input("Ingresar prioridad (1:R, 2:A, 3:V: ")) # la variable "element_2" contiene la prioridad a definir en cada ciclo
    #get_prioridad()

    def get_prioridad():

        if element_2==1:
            priority="importante"

        elif element_2==2:
            priority="intermedi"
        elif element_2==3:
            priority="baja"
        else:
            priority>3
            print("ingrese codigo correcto: 1, 2 ó 3")
            return get_prioridad()

""""
    if element_2==1:
        priority="importante"
    elif element_2==2:
        priority="intermedi"
    elif element_2==3:
        priority="baja"
    else:
        priority=str(0)
        print("ingrese codigo correcto: 1, 2 ó 3")
#falta que repita la pregunta hast que ingrese un valor correcto.
"""
tasks.append(aux) # se agrega el ID en la lista "task"
tasks.append(element_1) #se guarda la respuesta en la lista "task"
file.write(str(aux) + " | " + element_1 +" "+ priority) # + " | " + str(times)) #write es un metodo, se guarda la info de la lista
file.write('\n') #con esto se logra que este uno debajo de otro 
print(tasks) 


file.close() 


