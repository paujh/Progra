#Garcia Azamar Cristopher Alejandro
#8 de abril de 2019
#Descripcion: este programa permite gestionar los productos de una tienda para cubrir necesidades basicas.

class Producto:
	caja = 0
	def __init__(self,nombre,precio,cantidadDisponible):
		self.nombre = nombre
		self.precio = precio
		self.cantidadDisponible = cantidadDisponible

	def __str__(self): #Muestra la info del producto
		cadena = "Detalles: \n" + "\tNombre: " + self.nombre + "\n" + "\tPrecio: " + str(self.precio) + "\n" + "\tCantidad: " + str(self.cantidadDisponible)
		return cadena

