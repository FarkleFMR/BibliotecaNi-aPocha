LibroDB = [["Mamita Yunai",["Carlos Luis Fallas"],"Soley y Valverde",7,True,True],
           ["La Nariz",["Nikolái Gógol"],"Gadir",12,False,True],
           ["El lenguaje de programación C",["Brian Kernighan","Dennis Ritchie"],"Prentice Hall",2,False,True]]
ClienteDB = [["JenaMuri","Jenaro","Murillo","jenaromurilloaldecoba@gmail.com","24/09/1997"],
             ["JoseAcu","Jose","Acuña","joseacunacarrera@gmail.com","27/6/1999"]]


class Prestamo:
    def _init_(self,Id,Username,Libros,FechaPrestamo,FechaDevolucion,Activo):
        self.Id = Id
        self.Username = Username
        self.Libros = Libros
        self.FechaPrestamo = FechaPrestamo
        self.FechaDevolucion = FechaDevolucion
        self.Activo = Activo

class Devolucion:
    def _init_(self,Id,Username,Libros,FechaDevolucion):
        self.Id = Id
        self.Username = Username
        self.Libros = Libros
        self.FechaDevolucion = FechaDevolucion

class RegistrarPrestamosUI:
    def registrarPrestamo(self):
        print("Crear prestamo")
    def clickSeleccionarLibros(self):
        print("Lista de libros dispinibles")
    def clickContinuar(self):
        print("Lista de libros seleccionados")
    def IngresarDetalles(self,username,fechainicio,fechaDev,listaLibros):
        print("Ingresa detalles clase prestamo")
    def clickRegistrar(self,prestamo):
        print("Crea la clase")
    def enviarConfirmacion(self):
        print("Se ha ejecutado con exito")
    def enviarError(Self):
        print("Error")

class RegistrarPrestamoController:
    def mostrarLibros(self):
        print("Muestra los libros disponibles")
    def validaDatos(self,prestamo):
        print("Valida los datos")
        
class LibreriaDB:
    def mostrarLibros(self):
        print("Envia los libros disponibles")
    def IngresaSolicitud(self,prestamo):
        print("Agrega a la base de datos y de prestamo")
    def consultarinfoPrestamo(self,idPedido):
        print("Devuelve la info del prestamo")

class RegistrarDevUI:
    def registrarDevolucion(self):
        print("Crear devolucion")
    def insertarInfo(self,idPedido,fechaDev):
        print("Inserta la información")
    def mostrarInfoPrestamo(self,prestamo):
        print("Muestra info del prestamo ingresado")
    def clickDevolver(self):
        print("Crea la clase")
    def enviarConfirmacion(self):
        print("Se ha ejecutado con exito")
    def enviarError(Self):
        print("Error")
class RegistrarDevolucionController:
    def consultarInfo(self,idPedido,fechaDev):
        print("Va a buscar el pedido")
        
    
