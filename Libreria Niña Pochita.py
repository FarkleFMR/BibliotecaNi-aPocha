from tkinter import *
from tkinter import ttk
import tkinter as tk

class Autor:
    def __init__(self,nombre,apellido,nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

class Libro:
    def __init__(self,titulo,autor,editorial,ediccion,prestado):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ediccion = ediccion
        self.prestado = prestado
        self.activo = True

class Cliente:
    def __init__(self,username,nombre,apellido,email,fechaNacimiento):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fechaNacimiento = fechaNacimiento

a1 = Autor("Carlos Luis","Fallas","Costarricense")
a2 = Autor("Nikolái","Gógol","Ucraniano")
a3 = Autor("Brian","Kernighan","Canadiense")
a4 = Autor("Dennis","Ritchie","Estadounidense")

l1 = Libro("Mamita Yunai",[a1],"Soley y Valverde",7,False)
l2 = Libro("La Nariz",[a2],"Gadir",12,False)
l3 = Libro("El lenguaje de programación C",[a3,a4],"Prentice Hall",2,False)

c1 = Cliente("JenaMuri","Jenaro","Murillo","jenaromurilloaldecoba@gmail.com","24/09/1997")
c2 = Cliente("JoseAcu","Jose","Acuña","joseacunacarrera@gmail.com","27/6/1999")
LibroDB = [l1,l2,l3]
ClienteDB = [c1,c2]

class Prestamo:
    def __init__(self,Id,Username,Libros,FechaPrestamo,FechaDevolucion,Activo):
        self.Id = Id
        self.Username = Username
        self.Libros = Libros
        self.FechaPrestamo = FechaPrestamo
        self.FechaDevolucion = FechaDevolucion
        self.Activo = Activo

class Devolucion:
    def __init__(self,Id,Username,Libros,FechaDevolucion):
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
        
class MenuUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.titulo = tk.Label(self)
        self.titulo["text"] = "Libreria Niña Pochita"
        self.titulo["font"] = 30
        self.titulo.pack(side="top", padx=20,pady=10)
        self.gestlibros = tk.Button(self)
        self.gestlibros["text"] = "Gestionar Libros"
        self.gestlibros["width"] = 15
        self.gestlibros.pack(side="top", pady=10)
        self.registp = tk.Button(self)
        self.registp["text"] = "Registrar Préstamo"
        self.registp["width"] = 15
        self.registp.pack(side="top", pady=10)
        self.registd = tk.Button(self)
        self.registd["text"] = "Registrar Devolución"
        self.registd["width"] = 15
        self.registd.pack(side="top", pady=10)
        self.verlibros = tk.Button(self)
        self.verlibros["text"] = "Ver Libros"
        self.verlibros["width"] = 15
        self.verlibros.pack(side="top", pady=10)

class MenuController:
    root = Tk()
    app = MenuUI(master = root)
    app.mainloop()
MenuController()


