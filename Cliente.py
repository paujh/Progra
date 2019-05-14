#Garcia Azamar Cristopher Alejandro
#8 de abril de 2019
#Descripcion: este programa permite gestionar los productos de una tienda para cubrir necesidades basicas.

from Carrito import *

class Cliente:
	def __init__(self,nombre,edad,direccion,saldo): 
		self.nombre = nombre 
		self.edad = edad #cadena de caracteres
		self.direccion = direccion
		self.saldo = saldo #flotante	
		self.carrito = []

	def __str__(self): #Muestra la info. del cliente.
		cadena = "Detalles: \n" + "\tNombre: " + self.nombre + "\n" + "\tEdad: " + self.edad + "\n" + "\tDireccion: " + self.direccion + "\n" + "\tSaldo: " + str(self.saldo)
		return cadena

	def agregarCarrito(self,productoPorComprar): #Agrega un prductos definido por el usuario al carrito del cliente.
		carrito_cliente = Carrito()
		carrito_cliente.agregar(productoPorComprar)
		self.carrito = carrito_cliente.ListaProductos

	def eliminarProducto(self,productoPorEliminar): #Elimina un producto del carrito del cliente.
		ListaTemporal = []
		for i in range(0,len(self.carrito)):
			if self.carrito[i].nombre != productoPorEliminar:
				ListaTemporal.append(self.carrito[i])
			else:
				pass
		self.carrito = ListaTemporal

	def comprar(self): #Permite realizar la compra de los productos del carrito, considerando el saldo del cliente.
		Total = 0
		for i in range(0,len(self.carrito)):
			Total = Total + self.carrito[i].precio
		if float(Total) <= float(self.saldo):
			self.saldo = float(self.saldo) - float(Total)
			print("\n ¡Tu compra se ha realizado con exito! \n")
			print("Tu saldo restante es: \n\t",self.saldo)
		else:
			print("\n No tienes saldo suficiente, te hacen falta ", Total - self.saldo ," para finalizar la compra.\n ")

#Detalles pendientes: Hacer que el programa reste en una unidad la cantidad de articulos en existencia de un producto particular al realizar una compra.






		

	



