#Garcia Azamar Cristopher Alejandro
#8 de abril de 2019
#Descripcion: este programa permite gestionar los productos de una tienda para cubrir necesidades basicas.

from Cliente import *


class Tienda:
	nombre = "Doña Chuy abarrotes"
	almacen = []

	def set_almacen(): #Es necesario llamar a este metodo antes de trabajar propiamente con los objetos de esta clase.
		Tienda.almacen.append(Producto("Chetos",10,500))
		Tienda.almacen.append(Producto("iphone",30000,1000))
		Tienda.almacen.append(Producto("PlayStation",5000,200))
		Tienda.almacen.append(Producto("Tio Nacho",100,200))

	def __init__(self,cliente):
		self.cliente = cliente

	def __str__(self): #Muestra los detalles del cliente 
		cadena = self.cliente.__str__()
		return cadena

	def verAlmacen_agregar(self): #Muestra los productos disponibles en la tienda
									#Pregunta al usuario si desea agregar un articulo a su carrito. 
		print("\tNuestros productos: \n")
		for i in range (0,len(Tienda.almacen)):
			print("\t",Tienda.almacen[i].nombre,"\n")
			print("\tPrecio: ",Tienda.almacen[i].precio,"\n")
			print("\tUnidades disponibles: ",Tienda.almacen[i].cantidadDisponible,"\n")
		
		desicion = input("¿Desea agregar algo a su carrito?\n\t Responda SI/NO\n")
		
		if desicion == "SI":
			ProductoPorAgregar = input("Ingrese el nombre del articulo que desea: ")
			for i in range (0,len(Tienda.almacen)):
				if ProductoPorAgregar == Tienda.almacen[i].nombre:
					self.cliente.carrito.append(Tienda.almacen[i])
					print("Ha agregado",ProductoPorAgregar,"a su carrito")
					Tienda.almacen[i].cantidadDisponible = Tienda.almacen[i].cantidadDisponible-1
					break

				else:
					continue
					

		elif desicion == "NO":
			pass
		else:
			pass

	def eliminar(self,productoPorEliminar):
		self.cliente.eliminarProducto(productoPorEliminar)
		print("\nSe ha eliminado",productoPorEliminar,"de su carrito.\n")



	def comprar(self): #Permite realizar compras del carrito, considerando el saldo del cliente registrado.
		Total = 0
		for i in range(0,len(self.cliente.carrito)):
			Total = float(Total) + float(self.cliente.carrito[i].precio)
		if float(Total) <= float(self.cliente.saldo):
			self.cliente.saldo = float(self.cliente.saldo)-float(Total)
			print("\n ¡Tu compra se ha realizado con exito! \n")
			print("Tu saldo restante es: \n\t",self.cliente.saldo)
		else:
			print("\n No tienes saldo suficiente, te hacen falta ", float(Total) - float(self.cliente.saldo) ," para finalizar la compra.\n ")











		
	
