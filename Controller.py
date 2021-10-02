from datetime import datetime
from Model import *
from View import *

class PrestamoController:#Controlador
    def __init__(self, master):#Inicia todas las clases que necesita
        self.libroBD = LibrosDB()
        self.clienteBD = ClientesDB()
        self.prestamoUI = RegistrarPrestamosUI(master, self)
        self.prestamo = PrestamoDB()
        self.datos = []
        self.libro = ""
    def registrarPrestamo(self, datos):#Empieza la opcion de prestamos
        #Guarda el libro seleccionado de los libros disponibles, despues de
        #haberse comunicado con la basse de datos de libros para mostrar los
        #disponibles
        if self.validar_datos(datos):#Valida los datos
            self.datos = datos
            self.prestamoUI.mostrardisponibles(self.mostrar_libros())
        else:
            self.prestamoUI.mostrarError(1)#Error de validacion
    def seleccionarLibro(self, libro):
        if libro in self.mostrar_libros():#Si no se selecciono un libro
            self.prestamoUI.mostrarError(3)#Error
        else:
            self.libro = libro
            self.registrarprestamo(self.datos, self.libro)
            self.mostrar_prestamo(self.datos[0])
    def mostrar_libros(self):#Se comunica con la Base de datos
                            #libro para ver los disponibles
        libros = self.libroBD.getLibros()#Guarda los datos que le da la base
        return libros
    def validar_datos(self,datos):#Valida los datos ingresados
        if (self.clienteBD.isCliente(datos[0])):#Si existe el usuario
            try:
                #Valide las fechas
                datetime.strptime(datos[1],'%Y-%m-%d')
                datetime.strptime(datos[2],'%Y-%m-%d')
            except ValueError:
                #Error de fechas
                self.prestamoUI.mostrarError(2)
                return False
            return True
        else:
            return False
    #Se conecta con la base para obtener los datos del prestamo y luego lo pasa
    #a la capa de interfaz
    def mostrar_prestamo(self,username):
        print(PedidosDB[0].Username)
        info = self.prestamo.getPrestamo(username)
        self.prestamoUI.mostrarprestamo(info)
    #Crea el prestamo,se comunica con la base de datos de libro para que se registre
    #el libro como prestado        
    def registrarprestamo(self,datos,tituloLibro):
        #Crea el prestamo
        libro = self.libroBD.getByName(tituloLibro)
        p = Prestamo(datos[0]+datos[2][-2:]+datos[2][5:7],datos[0],libro,datos[1],datos[2])
        self.libroBD.setPrestamo(tituloLibro)#Cambia de estado el libro
        global PedidosDB
        PedidosDB += [p]#Lo guarda en la base
        

class DevolucionController():#Controlador de devolucion
    def __init__(self, master):#Inicializa las clases necesarias
        self.prestamo = PrestamoDB()
        self.libroBD = LibrosDB()
        self.devolucionUI = RegistroDevolucionUI(master, self)
        self.devolucion = DevoDB()

    def ingresarDatos(self, datos):#Se comunica con la capa UI para empezarla
        if self.validar_datos(datos):#Valida los datos
            self.mostrar_prestamo(datos[0])#Se comunica con UI y BD para mostrar prestamo
            self.registrardevolucion(datos)#Registra la devolucion
            self.devolucionUI.confirmarRegistro()#Se comunica con UI para mensaje exito
            self.mostrar_devolucion(datos[0])#Se comunica con UI y BD para mostrar devolucion
            
    def validar_datos(self,datos):#Valida los datos ingresados
        if self.prestamo.isPrestamo(datos[0]):#Si existe el prestamo
            try:
                datetime.strptime(datos[1],'%Y-%m-%d')#Valida fecha
            except ValueError:
                self.devolucionUI.mostrarError(2)#Le indica a la UI que mande error
                return False
            return True
        else:
            self.devolucionUI.mostrarError(1)#Le indica a la UI que mande error
            return False
    def mostrar_prestamo(self,Id):#Se comunica con la UI y BD para mostrar prestamo
        info = self.prestamo.getPrestamobyId(Id)#Le pide a BD que envie los datos
        self.devolucionUI.mostrarprestamo(info)#Le dice a la UI que ponga los datos
    def registrardevolucion(self,datos):#Crea la devolucion y hace los cambios
        prest = self.prestamo.getPrestamobyId(datos[0])#Adquiere los datos de prestamo
        d = Devolucion(datos[0],prest[1],prest[2],datos[1])#Registra la devolucion
        self.libroBD.setDevolucion(prest[2])#Libro cambia de estatus a disponible
        self.prestamo.devuelto(prest[0])#Inactiva el prestamo
        global DevolucionDB
        DevolucionDB += [d]#Agrega a base
    def mostrar_devolucion(self,Id):#Se comunica con la UI y BD para mostrar devolucion
        info = self.devolucion.getDevolucion(Id)#Le pide a BD que envie los datos
        self.devolucionUI.mostrardevo(info)#Le dice a la UI que ponga los datos

class MenuControler: #Controlador del menu
    def __init__(self):
        # Crea el ui del menu
        self.root = Tk()
        self.root.geometry("200x300")
        self.menuUI = MenuUI(self.root, self)
        self.root.mainloop()

    def registrarPrestamo(self):
        prestamoController = PrestamoController(self.root)

    def registrarDevolucion(self):
        devolucionController = DevolucionController(self.root)

Menu = MenuControler()


