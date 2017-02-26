#-------------------------------------------------------------CLASE NODO---------------------------------------------------------------
class Nodo(object):
    """docstring for Nodo"""
    def __init__(self,datos,ind,node= None):
       self.data = datos
       self.siguienteNodo = node
       self.indicie= ind 

    def getSiguiente(self):
        return self.siguienteNodo

    def setSiguiente(self,node):
        self.siguienteNodo=node

    def getData(self):
        return self.data
    def setData(self,datos):
        self.data = datos

    def getIndice(self):
        return self.indicie
#------------------------------------------------------------------------CLASE LISTA--------------------------------------------------------
class Lista(object):
    """docstring for Lista"""
    def __init__(self, Primero=None):
        self.PrimerNodo = Primero
        self.size= 0

    def getSize(self):
        return self.size

    def Eliminar (self, ind):
        Actual = self.PrimerNodo
        prev_node = None

        while Actual:
            if Actual.getIndice() == ind:
                if prev_node:
                    prev_node.setSiguiente(Actual.getSiguiente())
                else:
                    self.PrimerNodo = Actual.getSiguiente()
                self.size -= 1
                return True     
            else:
                prev_node = Actual
                Actual = Actual.getSiguiente()
        return False  

    def AgregarNodo(self,datos):
        Nuevo = Nodo(datos,self.size,self.PrimerNodo)
        self.PrimerNodo = Nuevo
        self.size +=1

    def Buscar(self,dato):
        Actual = self.PrimerNodo

        while Actual:
            if Actual.getData()==dato:
                return Actual.getIndice()
            else:
                Actual = Actual.getSiguiente()
        return "No Existe el Dato"

#-------------------------------------------------CLASE COLA------------------------------------------------------------------------------
class Cola(object):
    """docstring for Cola"""
    def __init__(self):
        self.Primer = None
        self.Ultimo = None
        self.size=0

    def queue(self,dato):
        Nuevo = Nodo(dato,self.size)
        if self.Ultimo:
                self.Ultimo.setSiguiente(Nuevo)
                self.Ultimo=Nuevo
                print(str(dato))
        else:
                self.Primer=Nuevo
                self.Ultimo=Nuevo
                print(str(dato))

    def dequeue(self):
            if self.Primer:
                valor = self.Primer.getData()
                
                print(str(valor))
            if  self.Primer==self.Ultimo:
                self.Primer=self.Ultimo=None
                return "Ya No quedan Mas elementos en la Cola"
            else:
                self.Primer = self.Primer.getSiguiente()
            return valor

#----------------------------------------------------CLASE PILA----------------------------------------------------------------------------
class Pila(object):
    """docstring for Pila"""
    def __init__(self):
        self.First= None
        self.Last=None
        self.size=0

    def Push(self,obj):
        Nuevo = Nodo(obj,self.size,self.First)
        self.First = Nuevo
        self.size +=1

    def Pop(self):
        if self.First:
                valor = self.First.getData()
                
                print(str(valor))
        if  self.First==self.Last:
                self.First=self.Last=None
                return "Ya No quedan Mas elementos en la Cola"
        else:
                self.First = self.First.getSiguiente()
                return valor

MyPila = Pila()
MyPila.Push("Andrea")
MyPila.Push("Diego")
MyPila.Push("Lizett")
MyPila.Pop()
MyPila.Pop()












