name_dogs=[]
name_dogs=["boby", True, 10.5] #es una lista
print(name_dogs)
print(type(name_dogs))
print(len(name_dogs)) #len, es longitud (length)
print(name_dogs.index("boby")) # el "." es un metodo
print(name_dogs.index(True))
name_dogs.append("blanquita") #objeto.metodo, append es añadir
print(name_dogs)
print(name_dogs[-1]) #al poner un número negativo empieza de atras hacia adelante
print(name_dogs[1]) #al poner un número positivo empieza de adelante
name_dogs[1]=False
print(name_dogs)
print("blanquita" in name_dogs) #in viene de pertenencia
print("wow wow" in name_dogs)
