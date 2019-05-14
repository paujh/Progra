#Garcia Azamar Cristopher Alejandro
#8 de abril de 2019
#Version basica del carrito donde guardaremos los productos de la tienda.

from Producto import *

class Carrito: 
	def __init__(self):
		self.ListaProductos = []
	
	def agregar(self,productoPorComprar): #cada producto agregado cuenta por una sola unidad
		self.ListaProductos.append(productoPorComprar)
	
	
	def eliminar(self,elementoPorEliminar): #elimina un elemento del carrito, en base al nombre exacto de este.
		ListaTemporal = []
		for i in range(0,len(self.ListaProductos)):
			if self.ListaProductos[i].nombre != elementoPorEliminar:
				ListaTemporal.append(self.ListaProductos[i])
			else:
				pass
		self.ListaProductos = ListaTemporal
	
	def comprar(self): #permite realizar compras (de manera primitiva)
		Total = 0
		for i in range(0,len(self.ListaProductos)):
			Total = Total + self.ListaProductos[i].precio
		return Total
		








