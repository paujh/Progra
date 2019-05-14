#Garcia Azamar Cristopher Alejandro
#8 de abril de 2019

from Tienda import *

class Menu:
	def __init__(self):
		pass
	
	def registrarCliente(self): #Registra el cliente y lo guarda en una lista como atributo dentro del constructor.
								#Por el momento solo registrar un cliente.
		nombre = input("Introduzca su nombre: ")
		edad = input("Introduzca su edad: ")
		direccion = input("Introduzca su direccion: ")
		saldo = input("Introduzca su saldo: ")
		cliente = Tienda(Cliente(nombre,edad,direccion,saldo))
		cliente.verAlmacen_agregar()
		while 0<1:
			eleccion=input("\n¿Que desea hacer?:\n\ta)Regresar al carrito\tb)Comprar\tc)Eliminar producto del carrito\nSeleccione a,b ó c: ")
			if eleccion =="a":
				cliente.verAlmacen_agregar()
			elif eleccion =="b":
				cliente.comprar()
			elif eleccion =="c":
				Eliminacion = input("\nIntroduzca el nombre del articulo que desea eliminar: ")
				cliente.eliminar(Eliminacion)




	


		#Notas: Para la correcta ejecución del programa tener en cuenta lo siguiente:
		
		#1) El metodo Tienda.set_almacen() debe ir al inicio para inicializar el almacen de la Tienda con Productos, pues de lo contrario estara vacia
		#2) Por el momento solo sera posible registrar un cliente por cada objeto de la tienda.

		# Por ahora Menu permite al usuario registrar clientes, añadir productos al carrito y realizar compras.
		#Queda pendiente definir en esta clase el metodo "eliminar" (presente en las clases Carrito y Cliente), el cual elimina articulos del carrito del cliente.
		#Otro detalle pendiente es hacer que el programa reste en una unidad la cantidad de articulos en existencia de un producto particular de la Tienda al realizar una compra.
		
		#Por cuestiones de mi editor de codigo, el codigo ejemplo para verificar el funcionamiento del programa es el siguiente:
			#import Menu from *
			#Tienda.set_almacen()
			#registro_1 = Menu()
			#...El usuuario ingresa los datos del cliente.
			#registro_1.verAlmacen_agregar()
			#...En este metodo el usuario puede decidir si agregar articulos a su carrito o no, y en caso de aceptar, escribir el nombre de aquellos de su interes.
			#registro_1.comprar()
		#De igual forma se agrega el archivo de las pruebas con el formato mediante el cual me fue posible realizarlas.





