#Garcia Azamar Cristopher Alejandro
#8 de abril de 2019
#Campo de prueba de nuestras clases.

from Menu import *

#Pruebas carrito

carrito_1=Carrito()
carrito_1.agregar(Producto("Chetos",5,500))
carrito_1.agregar(Producto("Gamesa",5,500))
carrito_1.agregar(Producto("Barcel",5,500))
print(carrito_1.ListaProductos)
print(carrito_1.ListaProductos[0].nombre)
print(carrito_1.ListaProductos[1].nombre)
print(carrito_1.ListaProductos[2].nombre)
carrito_1.eliminar("Gamesa")
print(carrito_1.ListaProductos)
print(carrito_1.ListaProductos[0].nombre)
print(carrito_1.ListaProductos[1].nombre)
print(carrito_1.comprar())

#Pruebas Cliente

cliente_1=Cliente("Miguel","17","Ecatepec",100)
print(cliente_1)
cliente_1.agregarCarrito(Producto("samsung",5000,20))
print(cliente_1.carrito[0].nombre)
cliente_1.comprar()
cliente_2=Cliente("Rosaura","20","Santa Fe",1000000)
cliente_2.agregarCarrito(Producto("iphone XS",50000,20))
cliente_2.comprar()


