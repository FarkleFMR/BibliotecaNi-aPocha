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
        self.getByName(libro).prestado = True
    def setDevolucion(self,libro):#Busca el libro prestado y le cambia el estatus
                                #a disponible
        for i in range(len(LibroDB)):
            if LibroDB[i] == libro:
                LibroDB[i].prestado = False
                break
    def getByName(self, libro):
        for i in range(len(LibroDB)):
            if LibroDB[i].titulo == libro:
                return LibroDB[i]
        

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
            print(PedidosDB[i].Username, username)
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