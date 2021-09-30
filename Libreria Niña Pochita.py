from datetime import datetime
class Autor: #Clase autor
    def __init__(self,nombre,apellido,nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

class Libro: #Clase libro
    def __init__(self,titulo,autor,editorial,ediccion,prestado):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ediccion = ediccion
        self.prestado = prestado
        self.activo = True

class Cliente: #Clase Cliente
    def __init__(self,username,nombre,apellido,email,fechaNacimiento):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fechaNacimiento = fechaNacimiento

class Prestamo: #Clase Prestamo
    def __init__(self,Id,Username,Libros,FechaPrestamo,FechaDevolucion):
        self.Id = Id
        self.Username = Username
        self.Libros = Libros
        self.FechaPrestamo = FechaPrestamo
        self.FechaDevolucion = FechaDevolucion
        self.Activo = True
        

class Devolucion: #Clase Devolución
    def __init__(self,Id,Username,Libros,FechaDevolucion):
        self.Id = Id
        self.Username = Username
        self.Libros = Libros
        self.FechaDevolucion = FechaDevolucion
#Se crean autores
a1 = Autor("Carlos Luis","Fallas","Costarricense")
a2 = Autor("Nikolái","Gógol","Ucraniano")
a3 = Autor("Brian","Kernighan","Canadiense")
a4 = Autor("Dennis","Ritchie","Estadounidense")
#Se crean libros
l1 = Libro("Mamita Yunai",[a1],"Soley y Valverde",7,False)
l2 = Libro("La Nariz",[a2],"Gadir",12,False)
l3 = Libro("El lenguaje de programación C",[a3,a4],"Prentice Hall",2,False)
#Se crean estudiantes
c1 = Cliente("JenaMuri","Jenaro","Murillo","jenaromurilloaldecoba@gmail.com","24/09/1997")
c2 = Cliente("JoseAcu","Jose","Acuña","joseacunacarrera@gmail.com","27/6/1999")


#Base de datos
LibroDB = [l1,l2,l3]
ClienteDB = [c1,c2]
PedidosDB = []
DevolucionDB = []

class LibrosDB:#Clase que se comunica con la base de datos de libros
    def __init__(self):
        pass
    def getLibros(self):#Obtiene todos los libros disponibles
        disponibles = []
        for i in range(len(LibroDB)):#Busca en la base de datos
            if(LibroDB[i].prestado == False):#Si se encuentre disponible
                disponibles += [LibroDB[i]]#Agrega a la lista disponibles
        return disponibles#Retorna la lista de los libros disponibles
    def setPrestamo(self,libro):#Cambia el estatus a prestado
        LibroDB[libro].prestado = True
    def setDevolucion(self,libro):#Busca el libro prestado y le cambia el estatus
                                #a disponible
        for i in range(len(LibroDB)):
            if LibroDB[i] == libro:
                LibroDB[i].prestado = False
                break
        

class ClientesDB:#Clase que se comunica con la base de datos de clientes
    def __init__(self):
        pass
    def isCliente(self,username):#Busca si el cliente dado existe
        for i in range(len(ClienteDB)):
            if(ClienteDB[i].username == username):
                return True
        return False

class PrestamoDB:#Clase que se comunica con la base de datos de prestamos
    def __init__(self):
        pass
    def getPrestamo(self,username):#Obtiene la informacion de prestamo por username
        info = []
        for i in range(len(PedidosDB)):#Recorre la base
            #Si encuentra el username y el pedido esta activo
            if(PedidosDB[i].Username == username and PedidosDB[i].Activo == True):
                #Guarda la info del prestamo
                info = [PedidosDB[i].Id,PedidosDB[i].Username,PedidosDB[i].Libros.titulo,PedidosDB[i].FechaPrestamo,PedidosDB[i].FechaDevolucion]
                break
        return info#La retorna
    def getPrestamobyId(self,Id):#Lo mismo que getPrestamo pero con Id
        info = []
        for i in range(len(PedidosDB)):
            if(PedidosDB[i].Id == Id):
                info = [PedidosDB[i].Id,PedidosDB[i].Username,PedidosDB[i].Libros.titulo,PedidosDB[i].FechaPrestamo,PedidosDB[i].FechaDevolucion]
                break
        return info
    def isPrestamo(self,Id):#Busca la existencia del prestamo
        for i in range(len(PedidosDB)):
            if(PedidosDB[i].Id == Id):
                return True
        return False
    def devuelto(self,Id):#Cambia el estatus del prestamo de activo a inactivo
        for i in range(len(PedidosDB)):
            if(PedidosDB[i].Id == Id):
                PedidosDB[i].Activo = False
                break
            
class DevoDB: #Clase que se comunica con la base de datos de devoluciones
    def __init__(self):
        pass
    def getDevolucion(self,Id):#Obtiene la informacion de la devolucion
        info = []
        for i in range(len(DevolucionDB)):#Recorre la base
            if(DevolucionDB[i].Id == Id):#Si encuentra la devolucion que busco
                #Guarda los datos
                info = [DevolucionDB[i].Id,DevolucionDB[i].Username,DevolucionDB[i].Libros,DevolucionDB[i].FechaDevolucion]
                break
        return info#Retorna los datos de la devolucion
class RegistrarPrestamosUI: #Clase que construye la interfaz de prestamos
    def __init__(self):
        pass
    def registrarPrestamo(self):#Crea la interfaz para que ingresen los datos
        print("Registrar prestamo:\n")
        username = input("Digite el username: ")
        fechaPrestamo = input("Digite la fecha de hoy (YYYY-MM-DD): ")
        fechaDevolucion = input("Digite la fecha de devolución (YYYY-MM-DD): ")
        datos = [username,fechaPrestamo,fechaDevolucion]
        return datos
    def mostrardisponibles(self,disponibles):#Crea la interfaz para mostrar
                                            #los libros disponibles
        print("Libros:")
        for i in range(len(disponibles)):
            print(str(i+1) + ": " + disponibles[i].titulo)
        opcion = input("Digite el libro a prestar: ")
        return int(opcion)-1
    def mostrarprestamo(self,info):#Muestra en la interfaz los datos del prestamo
        print("Prestamo:")
        print("Id: "+info[0])
        print("Username: "+info[1])
        print("Libro: "+info[2])
        print("Fecha: "+info[3])
        print("Fecha para devolver: "+info[4])
    def mostrarError(self,tipo): #Muestra en la interfaz el error dependiendo
                                #del tipo
        if tipo == 1:#Error en el username
            print("Error, Username no valido")
        elif tipo == 2:#Error en las fechas
            print("Error, Fecha no valida")
        elif tipo == 3:#Error en los libros
            print("Error, No existe el libro")
    def confirmarRegistro(self):#Mensaje que todo salio con exito
        print("El prestamo ha sido realizado con exito")
    

class PrestamoController:#Controlador
    def __init__(self):#Inicia todas las clases que necesita
        self.libroBD = LibrosDB()
        self.clienteBD = ClientesDB()
        self.prestamoUI = RegistrarPrestamosUI()
        self.prestamo = PrestamoDB()
    def mostrarIU(self):#Empieza la opcion de prestamos
        datos = self.prestamoUI.registrarPrestamo()#Guarda los datos ingresados
                                                    #en la interfaz
        #Guarda el libro seleccionado de los libros disponibles, despues de
        #haberse comunicado con la basse de datos de libros para mostrar los
        #disponibles
        libroselec = self.prestamoUI.mostrardisponibles(self.mostrar_libros())
        if libroselec > len(self.mostrar_libros()):#Si no se selecciono un libro
            self.prestamoUI.mostrarError(3)#Error
        if self.validar_datos(datos):#Valida los datos
            self.registrarprestamo(datos,libroselec)#Registra el prestamo
            self.mostrar_prestamo(datos[0])#Muestra los datos del prestamo creado
            self.prestamoUI.confirmarRegistro()#Se comunica con IU para decir exito
        else:
            self.prestamoUI.mostrarError(1)#Error de validacion
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
        info = self.prestamo.getPrestamo(username)
        self.prestamoUI.mostrarprestamo(info)
#Crea el prestamo,se comunica con la base de datos de libro para que se registre
#el libro como prestado        
    def registrarprestamo(self,datos,libro):
        #Crea el prestamo
        p = Prestamo(datos[0]+datos[2][-2:]+datos[2][5:7],datos[0],LibroDB[libro],datos[1],datos[2])
        self.libroBD.setPrestamo(libro)#Cambia de estado el libro
        global PedidosDB
        PedidosDB += [p]#Lo guarda en la base
        
class RegistroDevolucionUI():#Clase encargada de la UI de devolucion
    def __init__(self):
        pass
    def registrarDevolucion(self):#UI para ingreso de datos
        print("Registrar devolución:\n")
        Id = input("Digite el id del préstamo: ")
        fechaDevolución = input("Digite la fecha de la devolución (YYYY-MM-DD): ")
        datos = [Id,fechaDevolución]
        return datos
    def mostrarprestamo(self,info):#UI para mostrar datos del prestamo que se devuelve
        print("Prestamo:")
        print("Id: "+info[0])
        print("Username: "+info[1])
        print("Libro: "+info[2])
        print("Fecha: "+info[3])
        print("Fecha para devolver: "+info[4])
    def mostrardevo(self,info):#UI para mostrar los detalles de la devolucion
        print("Devolucion:")
        print("Id: "+info[0])
        print("Username: "+info[1])
        print("Libro: "+info[2])
        print("Fecha que se devolvio: "+info[3])
    def mostrarError(self,tipo):#Muestra los errores
        if tipo == 1:
            print("Error, Id no valido")#No existe el prestamo
        elif tipo == 2:
            print("Error, Fecha no valida")#Erro de fecha
    def confirmarRegistro(self):#Mensaje de exito
        print("La devolucion ha sido realizada con exito")
        
class DevolucionController():#Controlador de devolucion
    def __init__(self):#Inicializa las clases necesarias
        self.prestamo = PrestamoDB()
        self.libroBD = LibrosDB()
        self.devolucionUI = RegistroDevolucionUI()
        self.devolucion = DevoDB()
    def mostrarIU(self):#Se comunica con la capa UI para empezarla
        datos = self.devolucionUI.registrarDevolucion()#Guarda los datos de UI
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
        
class MenuUI:#Clase para inicia la UI de menu
    def __init__(self):
        pass
    def menu(self):
        print ("Libreria Niña Pochita")
        print("1.Registrar Prestamo")
        print("2.Registrar Devolución")
        print("3.Salir")
        opcion = input("Digite la opcion que desea realizar: ")
        return opcion
class MenuControler: #Controlador del menu
    def __init__(self):
        self.menuUI = MenuUI()
        self.prestamo = PrestamoController()
        self.devolucion = DevolucionController()
    def mostrarmenu(self):
        while True:
            opcion = self.menuUI.menu()
            if opcion == "1":
                self.prestamo.mostrarIU()
            elif opcion == "2":
                self.devolucion.mostrarIU()
            elif opcion == "3":
                break
            else:
                print("Error: Digite una opcion valida")
Menu = MenuControler()
Menu.mostrarmenu()


