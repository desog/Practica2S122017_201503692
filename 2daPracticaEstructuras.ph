class Nodo(object):
	"""docstring for ClassName"""
	def __init__(self, data):
		self.data = data
		self.siguiente = None
		self.anterior = None

"""CLASE LISTA"""
class Lista(object):
	"""docstring for Lista"""
	def __init__(self):
		self.Primero= None

	def agregar(self,data):
		node = Nodo(data)
		if self.Primero == None : 
			self.Primero = node 
		else : 
			node.siguiente = self.Primero
			node.siguiente.anterior = node
			self.Primero=node
			print (node)


	def Busqueda(self, k):
		p = self.Primero
		if p != None : 
				while p.siguiente != None:
					if(p.data == k) :
						return p
		return None

		
