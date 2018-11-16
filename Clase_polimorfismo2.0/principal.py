from paquete.modelado import * #importamos la clase modelado de el paquete
#persona = PersonaEquipo("Luis")

e = Entrenador("Jose") #Agregamos un argumento a la clase entrenador

f = Futbolista("Antonio") #Agregamos un argumento a la clase futbolista

m = MedicoEquipo("Ramón") #Agregamos un argumento a la clase medico equipo

p = PresidenteEquipo("Francisco") #Agregamos un argumento a la clase presidente equipo

lista = [f,m,p,e] #lista donde los elementos son clases con sus argumentos
for l in lista: # l recorre la lista 
	l.entrenar() # se presenta el objeto entrenar

