from tkinter import *
from tkinter import messagebox

class RegistrarPrestamosUI: #Clase que construye la interfaz de prestamos
    def __init__(self, master, controller):
        self.prestamoUI = Toplevel(master)
        self.prestamoUI.geometry("250x400")
        self.master = master
        #
        self.controller = controller
        #
        self.title = Label(self.prestamoUI, text="Registrar Prestamo")
        self.title.pack()
        self.usernameLbl = Label(self.prestamoUI, text="Nombre de usuario")
        self.usernameLbl.pack()
        self.username = Entry(self.prestamoUI)
        self.username.pack()
        self.fechaPrestamoLbl = Label(self.prestamoUI, text="Fecha de hoy (YYYY-MM-DD)")
        self.fechaPrestamoLbl.pack()
        self.fechaPrestamo = Entry(self.prestamoUI)
        self.fechaPrestamo.pack()
        self.fechaPrestamoLbl = Label(self.prestamoUI, text="Fecha de Devolucion (YYYY-MM-DD)")
        self.fechaPrestamoLbl.pack()
        self.fechaDevolucion = Entry(self.prestamoUI)
        self.fechaDevolucion.pack()
        self.buscarLibros = Button(self.prestamoUI, text="Ingresar Datos y Ver Libros", command=self.registrarPrestamo)
        self.buscarLibros.pack()
        self.listBoxLibros = Listbox(self.prestamoUI)
        self.listBoxLibros.pack()
        self.seleccionarLibrosBtn = Button(self.prestamoUI, text="Seleccionar Libro", command=self.seleccionarLibro)
        self.seleccionarLibrosBtn.pack()

    def registrarPrestamo(self):#Crea la interfaz para que ingresen los datos
        self.controller.registrarPrestamo([self.username.get(), self.fechaPrestamo.get(), self.fechaDevolucion.get()])
    def mostrardisponibles(self,disponibles):#Crea la interfaz para mostrar
                                            #los libros disponibles
        for i in range(len(disponibles)):
            self.listBoxLibros.insert(END, disponibles[i].titulo)
    def seleccionarLibro(self):
        self.controller.seleccionarLibro(self.listBoxLibros.get(self.listBoxLibros.curselection()))
        
    def mostrarprestamo(self,info):#Muestra en la interfaz los datos del prestamo
        messagebox.showinfo(message="Id: "+info[0]+"\nUsername: "+info[1]+"\nLibro: "+info[2]+"\nFecha: "+info[3]+"\nFecha para devolver: "+info[4], title="Prestamo")
        self.confirmarRegistro()
    def mostrarError(self,tipo): #Muestra en la interfaz el error dependiendo
                                #del tipo
        if tipo == 1:#Error en el username
            messagebox.showerror(message="Error, Username no valido", title="Error")
            print("Error, Username no valido")
        elif tipo == 2:#Error en las fechas
            messagebox.showerror(message="Error, Fecha no valida", title="Error")
            print("Error, Fecha no valida")
        elif tipo == 3:#Error en los libros
            messagebox.showerror(message="Error, No existe el libro", title="Error")
            print("Error, No existe el libro")
    def confirmarRegistro(self):#Mensaje que todo salio con exito
        messagebox.showinfo(message="El prestamo ha sido realizado con exito", title="Exito")
        print("El prestamo ha sido realizado con exito")
 
class RegistroDevolucionUI():#Clase encargada de la UI de devolucion
    def __init__(self, master, controller):
        self.devolucionUI = Toplevel(master)
        self.devolucionUI.geometry("250x400")
        self.master = master
        self.controller = controller
        #componentes de la UI
        self.title = Label(self.devolucionUI, text="Registrar Devolucion")
        self.title.pack()
        self.idLbl = Label(self.devolucionUI, text="Id del prestamo")
        self.idLbl.pack()
        self.Id = Entry(self.devolucionUI)
        self.Id.pack()
        self.fechaDevolucionLbl = Label(self.devolucionUI, text="Fecha de la devolución (YYYY-MM-DD)")
        self.fechaDevolucionLbl.pack()
        self.fechaDevolucion = Entry(self.devolucionUI)
        self.fechaDevolucion.pack()
        self.ingresarDatos = Button(self.devolucionUI, text="Ingresar Datos", command=self.registrarDevolucion)
        self.ingresarDatos.pack()

    def registrarDevolucion(self):#UI para ingreso de datos
        self.controller.ingresarDatos([self.Id.get(),self.fechaDevolucion.get()])

    def mostrarprestamo(self,info):#UI para mostrar datos del prestamo que se devuelve

        messagebox.showinfo(message="Id: "+info[0]+"\nUsername: "+info[1]+"\nLibro: "+info[2]+"\nFecha: "+info[3]+"\nFecha para devolver: "+info[4], title="Prestamo")

    def mostrardevo(self,info):#UI para mostrar los detalles de la devolucion
        messagebox.showinfo(message="Id: "+info[0]+"\nUsername: "+info[1]+"\nLibro: "+info[2]+"\nFecha que se devolvio: "+info[3], title="Devolucion")
    def mostrarError(self,tipo):#Muestra los errores
        if tipo == 1:
            messagebox.showerror(message="Error, Id no valido", title="Error")
            print("Error, Id no valido")#No existe el prestamo
        elif tipo == 2:
            messagebox.showerror(message="Error, Fecha no valida", title="Error")
            print("Error, Fecha no valida")#Erro de fecha
    def confirmarRegistro(self):#Mensaje de exito
        messagebox.showinfo(message="La devolucion ha sido realizada con exito", title="Exito")
        
class MenuUI:#Clase para inicia la UI de menu
    def __init__(self, master, controller):
        # se inicializa el frame
        menuFrame = Frame(master)
        menuFrame.pack()
        self.master = master
        self.controller = controller
        # se crean los elementos del UI
        self.title = Label(master, text="Libreria Niña Pochita")
        self.title.pack()
        self.registrarPrestamoBtn = Button(master, text="Registrar Prestamo", command=self.registrarPrestamo)
        self.registrarPrestamoBtn.pack()
        self.registrarDevolucionBtn = Button(master, text="Registrar Devolucion", command=self.registrarDevolucion)
        self.registrarDevolucionBtn.pack()
        self.salir = Button(master, text="Salir", command=menuFrame.quit)
        self.salir.pack()

    def registrarPrestamo(self):
        # se instancia el controller de registrar prestamos
        self.controller.registrarPrestamo()

    def registrarDevolucion(self):
        self.controller.registrarDevolucion()
