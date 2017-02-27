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
        self.UltimoNodo = None
        self.size= 0

    def getSize(self):
        return self.size

    def Eliminar (self, ind):
        i = 0
        Actual = self.PrimerNodo
        prev_node = None

        while Actual:
            if i == int(ind):
                if prev_node:
                    prev_node.setSiguiente(Actual.getSiguiente())
                else:
                    self.PrimerNodo = Actual.getSiguiente()
                self.size -= 1
                return Actual.getData()    
            else:
                prev_node = Actual
                Actual = Actual.getSiguiente()
                i+=1
        return "No se ha Podido Eliminar"

    def AgregarNodo(self,datos):
        Nuevo = Nodo(datos,self.size)
        if self.UltimoNodo:
                self.UltimoNodo.setSiguiente(Nuevo)
                self.UltimoNodo=Nuevo
                self.size +=1
        else:
                self.PrimerNodo=Nuevo
                self.UltimoNodo=Nuevo
                self.size +=1

    def Buscar(self,dato):
        i=0
        Actual = self.PrimerNodo

        while Actual:
            if Actual.getData()==dato:
                return i
            else:
                Actual = Actual.getSiguiente()
                i += 1
        return "No Existe el Dato"

        #Buscar por Indice
    def buscarIndice(self,index):
        i = 0
        Actual = self.PrimerNodo

        while Actual:
            if i==index:
                return Actual.getData()
            else:
                Actual = Actual.getSiguiente()
                i+=1
  

    def mostrar(self):
        if  not self.PrimerNodo:
            print("LA LISTA ESTA VACIA")
        Actual = self.PrimerNodo

        while Actual:
            print(str(Actual.getData()))
            Actual= Actual.getSiguiente()

# myLista = Lista()
# myLista.AgregarNodo("A")
# myLista.AgregarNodo("B")
# myLista.AgregarNodo("C")
# myLista.AgregarNodo("D")
# myLista.AgregarNodo("E")
# myLista.AgregarNodo("Diego")
# myLista.AgregarNodo("Andrea")
# print(str(myLista.Eliminar(3)))
# print(str(myLista.Eliminar(3)))

myLista = Lista()



        
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
                self.size +=1
        else:
                self.Primer=Nuevo
                self.Ultimo=Nuevo
                print(str(dato))
                self.size+=1

    def dequeue(self):
            if self.Primer:
                valor = self.Primer.getData()
                self.size-=1
                print(str(valor))
            if  self.Primer==self.Ultimo:
                self.Primer=self.Ultimo=None
                self.size=0
                return "Ya No quedan Mas elementos en la Cola"
            else:
                self.Primer = self.Primer.getSiguiente()
            return valor

    def getSize(self):
        return self.size

     #Buscar por Indice
    def buscarIndice(self,index):
        i = 0
        Actual = self.Primer

        while Actual:
            if i==index:
                return Actual.getData()
            else:
                Actual = Actual.getSiguiente()
                i+=1

myCola = Cola()
# myCola.queue("A")
# myCola.queue("B")
# myCola.queue("C")


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

#-----------------------------------------------------------------CLASE GRAFICA--------------------------------------------------------------
from graphviz import Digraph
class Reportes(object):
     """docstring for Reportes"""
     def __init__(self):
         self.datos = None

     def GrafoLista(self):
        

        dot = Digraph(comment='The Round Table')
        dot

        for x in xrange(0,myLista.getSize()):

            dot.node(str(x), str(myLista.buscarIndice(x)))
            if x!=myLista.getSize()-1:
                dot.edge(str(x),str(x+1), constraint='false')
                

            else:
                print("Hola")
                pass

            dot.render('Practica2S122017_201503692/Lista.gv', view=False)
            print(str(myLista.buscarIndice(x)))
            pass

#GRAFO COLA
    
     def GrafoCola(self):
            
        

            dot = Digraph(comment='The Round Table')
            dot

            for x in xrange(0,myCola.getSize()):

                dot.node(str(x), str(myCola.buscarIndice(x)))
                if x!=myCola.getSize()-1:
                    dot.edge(str(x),str(x+1), constraint='false')
                    print(str(myCola.buscarIndice(x)))

                else:
                    print("Hola")
                pass

            dot.render('Practica2S122017_201503692/Cola.gv', view=False)
            
            pass   



#-------------------------------------------------------------------FLASK------------------------------------------------------------
from flask import Flask, request, Response
app = Flask("Web Estructuras")
@app.route('/metodoWeb',methods=['POST']) 
def hello():
    parametro = str(request.form['dato'])
    myLista.AgregarNodo(parametro)
    Repor = Reportes()
    Repor.GrafoLista()
    return "HECHO"

@app.route('/eliminar',methods=['POST']) 
def delete():
    parametro = str(request.form['indice'])
    print(str(myLista.Eliminar(parametro)))

    Repor = Reportes()
    Repor.GrafoLista()
    return str(parametro + str())

@app.route('/busqueda',methods=['POST']) 
def BuscarLista():
    parametro = str(request.form['dato'])
    print(str(myLista.Eliminar(parametro)))

@app.route('/encolar',methods=['POST']) 
def Encolar():
    parametro = str(request.form['dato'])
    myCola.queue(parametro)
    Repor = Reportes()
    Repor.GrafoCola()
    return "HECHO"

@app.route('/desencolar',methods=['POST']) 
def eliminarcola():
    
    temp=(str(myCola.dequeue()))

    Repor = Reportes()
    Repor.GrafoCola()
    return str(temp)

    
    return str(myCola.Buscar())
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')








