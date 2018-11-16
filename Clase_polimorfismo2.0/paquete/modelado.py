import abc # importamos abc

class PersonaEquipo(metaclass=abc.ABCMeta): #esta clase padre donde el objeto es abstracto 
    """
        se define la clases abstracta
    """
    #__metaclass__ = abc.ABCMeta  #python 2
    
    def __init__(self, n):  # se define el __init__  con las variables a utilizar
        self.nombre = n

    @abc.abstractmethod # decorador para el metodo abstracto 
    
    #inicio del metodo abstracto
    def entrenar():
        pass

    #metodos para agregar y obtener
    def agregar_nombre (self, n):
        self.nombre = n
    
    def obtener_nombre (self):
        return self.nombre

    def entrenar(self): #metodo constructor
       print("yo %s " %(self.obtener_nombre()))


class Entrenador(PersonaEquipo): #Clase entrenador  donde recibe  metodos de la clase padre
    """
    """

    def __init__(self, n):  # se define el __init__  con las variables a utilizar
        super(Entrenador, self).__init__(n) #utilizamos el super para ocupar las funciones de la clase padre y le mandamos un argumento
        self.codigoEntrenador = "" #inicializacion de variable

    #metodos para agregar y obtener
    def setCodigo(self,c):
        self.codigoEntrenador = c

    def getCodigo(self):
        return self.codigoEntrenador

    def entrenar(self): #metodo constructor
        print("Yo %s, entrenador, soy el director del entrenamiento" %(self.obtener_nombre()))


class Futbolista(PersonaEquipo):
    
    def __init__(self,n):  # se define el __init__  con las variables a utilizar
        super(Futbolista, self).__init__(n) #utilizamos el super para ocupar las funciones de la clase padre y le mandamos un argumento
        self.posicionCampo = "" #inicializacion de variable

     #metodos para agregar y obtener
    def setPosicion(self,p):
        posicionCampo = p

    def getPosicion(self):
        return self.posicionCampo

    def entrenar(self): #metodo constructor
        print("Yo %s,Futbolista, Hago práctica en el entrenamiento"%(self.obtener_nombre()))


class MedicoEquipo(PersonaEquipo):
    
    def __init__(self,n):  # se define el __init__  con las variables a utilizar
        super(MedicoEquipo, self).__init__(n) #utilizamos el super para ocupar las funciones de la clase padre y le mandamos un argumento
        self.titulo = "" #inicializacion de variable

    
     #metodos para agregar y obtener
    def setPosicion(self,t):
        titulo = t

    def getPosicion(self):
        return self.titulo

    def entrenar(self): #metodo constructor
        print("Yo %s, Medico, atiendo a los jugadores del entrenamiento"%(self.obtener_nombre()))


class PresidenteEquipo(PersonaEquipo):
    
    def __init__(self,n):  # se define el __init__  con las variables a utilizar
        super(PresidenteEquipo, self).__init__(n) #utilizamos el super para ocupar las funciones de la clase padre y le mandamos un argumento
        self.propiedades = ""

    #metodos para agregar y obtener
    def setPosicion(self,p):
        propiedades = p

    def getPosicion(self):
        return self.propiedades

    def entrenar(self): #metodo constructor
        print("Yo %s, presidente, pongo dinero para el entrenamiento"%(self.obtener_nombre()))