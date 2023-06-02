from cProfile import label
from ctypes.wintypes import SHORT
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import tkinter as tk

from setuptools import Command
# Primero importamos todo y luego utilizamos Pillow para hacer uso de los diferentes formatos de imagenes.
window=tk.Tk()
window.geometry('900x500+300+120')
window.configure(bg= '#262626')#378fae')
window.resizable(0,0)
window.title('Razones de Rentabilidad')
var=tk.StringVar()
#en este caso resizable sirve para que la ventana no permita que se haga màs grande.
    

def default_home():
    f2=Frame(window, width=900, height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2, text="Home Financiera ​​❤️​​", fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 50))
    l2.place(x=190, y=150)

def home():
    f1.destroy()
    f2=Frame(window, width=900, height=455, bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2, text="Home Financiera", fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 50))
    l2.place(x=190, y=150)

#Creamos un funcion que nos limpia las cajas de texto donde ingresamos los datos
def limpiar():
       var.set("")
       ingresar1.delete(0, "end")
       ingresar2.delete(0, "end")
       return limpiar

def presentacion():
    f1.destroy()
    f2=Frame(window, width=900, height=455, bg='lightblue')
    f2.place(x=0, y=45)
    l2=Label(f2, text="Universiadad de las Regiones Autónomas de la", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 20))
    l2.place(x=130, y=40)
        
    l2=Label(f2, text="Costa caribe Nicaragüense", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 20))
    l2.place(x=250, y=80)

    l2=Label(f2, text="(URACCAN)", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 20))
    l2.place(x=350, y=120) 

    l2=Label(f2, text="⚖", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 60))
    l2.place(x=380, y=160) 

    l2=Label(f2, text="Elaborado por:", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 20))
    l2.place(x=350, y=300) 

    l2=Label(f2, text="Estudiantes del tercer año de Ingenieria en Sistemas", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 20))
    l2.place(x=120, y=350)

    def ven1():
        new_window = tk.Toplevel()
        new_window.title('Grupo #4')
        new_window.geometry('470x300+725+215')
        new_window.configure(bg='#deb3eb')
        new_window.resizable(0,0)

        l2=Label(new_window, text="Integrantes:", fg='#262626', bg='#deb3eb')
        l2.config(font=('Comic Sans MS', 20))
        l2.place(x=20, y=20)

        l2=Label(new_window, text="--> Jeyson Fernández", fg='#262626', bg='#deb3eb')
        l2.config(font=('Comic Sans MS', 15))
        l2.place(x=50, y=80)

        l2=Label(new_window, text="--> Diana Sanchez", fg='#262626', bg='#deb3eb')
        l2.config(font=('Comic Sans MS', 15))
        l2.place(x=50, y=110)

        l2=Label(new_window, text="--> Santos Alvarado", fg='#262626', bg='#deb3eb')
        l2.config(font=('Comic Sans MS', 15))
        l2.place(x=50, y=140)

        l2=Label(new_window, text="--> Anny Oyes", fg='#262626', bg='#deb3eb')
        l2.config(font=('Comic Sans MS', 15))
        l2.place(x=50, y=170)

        l2=Label(new_window, text="📆 Fecha:", fg='#262626', bg='#deb3eb')
        l2.config(font=('Comic Sans MS', 15))
        l2.place(x=300, y=200)

        l2=Label(new_window, text="04-05-2022", fg='#262626', bg='#deb3eb')
        l2.config(font=('Comic Sans MS', 15))
        l2.place(x=290, y=230)

        def cerrar_win():
            new_window.destroy()
            
        botonform1=tk.Button(new_window,text='<-Regresar-', bg='lightblue', fg='black', command=cerrar_win, padx=2, pady=2, width=10)
        botonform1.pack()
        botonform1.place(x=100, y=230)

    boton1=tk.Button(window, text="< Más >", bg='plum', fg='black', command=ven1, padx=5, pady=5, width=20)
    boton1.pack()
    boton1.place(x=370, y=450) 

def ren_inversion():
    f1.destroy()
    f2=Frame(window, width=900, height=455, bg='lightblue')
    f2.place(x=0, y=45)
    l2=Label(f2, text=" Bienvenido al apartado de Rendimiento de Inversión:", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 20))
    l2.place(x=110, y=20)

    l2=Label(f2, text="📈", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 30))
    l2.place(x=420, y=80)

    l4=Label(f2, text=" El Rendimiento de la Inversión, es utilizado para medir", fg='#262626', bg='lightblue')
    l4.config(font=('Comic Sans MS', 15))
    l4.place(x=190, y=170)

    l5=Label(f2, text="la cantidad de una inversión como proporción de la inversión inicial", fg='#262626', bg='lightblue')
    l5.config(font=('Comic Sans MS', 15))
    l5.place(x=140, y=200)
    #place es para pocicionar la letra.

    l9=tk.Label(f2, text="en terminos porcentuales", fg='#262626', bg='lightblue')
    l9.config(font=('Comic Sans MS', 15))
    l9.place(x=350, y=230)

    def ven1():
        global ingresar1, ingresar2

        new_window = tk.Toplevel()
        new_window.title('Rendimiento de inversión')
        new_window.geometry('470x300+925+315')
        new_window.configure(bg='lightblue')
        new_window.resizable(0,0)

        s1=tk.Label(new_window, text="Para resolverlo debemos conocer:", bg='#378fae', fg='black')
        s1.pack(padx=5, pady=10, ipadx=5, ipady=5, fill=tk.X)

        def formula1():
            formula1=float(ingresar1.get())/float(ingresar2.get())
            return var.set(formula1)

        s2=tk.Label(new_window, text="Utilidades despues de impuesto", bg='#fec8d8', fg='black')
        s2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        ingresar1=tk.Entry(new_window)
        ingresar1.pack(fill=tk.X, padx=5, ipadx=5, ipady=5)

        s3=tk.Label(new_window, text="Activos totales", bg='#fec8d8', fg='black')
        s3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        ingresar2=tk.Entry(new_window)
        ingresar2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        botonform1=tk.Button(new_window,text='Resultado', bg='plum', fg='black', command=formula1,  padx=2, pady=2, width=10)
        botonform1.pack(side=tk.RIGHT)
        botonform1.place(x=25, y=202)

        botonform1=tk.Button(new_window,text='Borrar', bg='plum', fg='black', command=limpiar, padx=2, pady=2, width=10)
        botonform1.pack(side=tk.LEFT)
        botonform1.place(x=360, y=202)

        result1=tk.Label(new_window, bg='lightgray', textvariable=var, padx=5, pady=5, width=30)
        result1.pack()

        def cerrar_win():
            new_window.destroy()
            
        botonform1=tk.Button(new_window,text='Cerrar', bg='#ff9aa2', fg='black', command=cerrar_win, padx=2, pady=2, width=10)
        botonform1.pack()
        botonform1.place(x=195, y=250)

    boton1=tk.Button(window, text="calcular", bg='plum', fg='black', command= ven1, padx=5, pady=5, width=30)
    boton1.pack(side=tk.TOP)
    boton1.place(x=350, y=400) 

def cap_social():
    f1.destroy()
    f2=Frame(window, width=900, height=455,bg='lightblue')
    f2.place(x=0, y=45)
    l2=Label(f2, text="Bienvenido al apartado de Rendimiento de Capital Social:", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 15))
    l2.place(x=190, y=20)

    l2=Label(f2, text="💰", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 30))
    l2.place(x=420, y=80)
    
    l4=Label(f2, text=" Es el valor de los bienes que posee la empresa y ", fg='#262626', bg='lightblue')
    l4.config(font=('Comic Sans MS', 15))
    l4.place(x=190, y=170)

    l5=Label(f2, text="  la aportación que realizan los socios,  el importe monetario   ", fg='#262626', bg='lightblue')
    l5.config(font=('Comic Sans MS', 15))
    l5.place(x=140, y=200)
    #place es para pocicionar la letra.

    l9=tk.Label(f2, text="de una  persona o un país.", fg='#262626', bg='lightblue')
    l9.config(font=('Comic Sans MS', 15))
    l9.place(x=300, y=230)

    def ven1():
        global ingresar1, ingresar2

        new_window = tk.Toplevel()
        new_window.title('Capital Social')
        new_window.geometry('470x300+725+215')
        new_window.configure(bg='lightblue')
        new_window.resizable(0,0)

        s1=tk.Label(new_window, text="Para resolverlo debemos conocer:", bg='lightblue', fg='black')
        s1.pack(padx=5, pady=10, ipadx=5, ipady=5, fill=tk.X)

        def formula1():
            formula1=float(ingresar1.get())/float(ingresar2.get())
            return var.set(formula1)

        s2=tk.Label(new_window, text="Utilidades netas después de impuesto", bg='#deb3eb', fg='black')
        s2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        ingresar1=tk.Entry(new_window)
        ingresar1.pack(fill=tk.X, padx=5, ipadx=5, ipady=5)

        s3=tk.Label(new_window, text="Capital de los accionistas", bg='#deb3eb', fg='black')
        s3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        ingresar2=tk.Entry(new_window)
        ingresar2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        botonform1=tk.Button(new_window,text='Resultado', bg='plum', fg='black', command=formula1,  padx=2, pady=2, width=10)
        botonform1.pack(side=tk.RIGHT)
        botonform1.place(x=25, y=202)

        botonform1=tk.Button(new_window,text='Borrar', bg='plum', fg='black', command=limpiar, padx=2, pady=2, width=10)
        botonform1.pack(side=tk.LEFT)
        botonform1.place(x=360, y=202)

        result1=tk.Label(new_window, bg='lightgray', textvariable=var, padx=5, pady=5, width=30)
        result1.pack()

        def cerrar_win():
            new_window.destroy()
            
        botonform1=tk.Button(new_window,text='Cerrar', bg='#ff9aa2', fg='black', command=cerrar_win, padx=2, pady=2, width=10)
        botonform1.pack()
        botonform1.place(x=195, y=250)

    boton1=tk.Button(window, text="calcular", bg='plum', fg='black', command= ven1, padx=5, pady=5, width=30)
    boton1.pack(side=tk.TOP)
    boton1.place(x=350, y=400)


def utilidades():
    f1.destroy()
    f2=Frame(window, width=900, height=455,bg='lightblue')
    f2.place(x=0, y=45)
    l2=Label(f2, text="Bienvenido al apartado de Utilidades por Acción:", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 15))
    l2.place(x=190, y=20)

    l2=Label(f2, text="📑", fg='#262626', bg='lightblue')
    l2.config(font=('Comic Sans MS', 30))
    l2.place(x=420, y=80)

    l4=Label(f2, text="Indica que se trata de los dividendos que", fg='#262626', bg='lightblue')
    l4.config(font=('Comic Sans MS', 15))
    l4.place(x=270, y=170)

    l5=Label(f2, text=" una empresa reparte a cada acción común en circulación", fg='#262626', bg='lightblue')
    l5.config(font=('Comic Sans MS', 15))
    l5.place(x=200, y=200)
    #place es para pocicionar la letra.
    
    l9=tk.Label(f2, text="sirve como indicador de la rentabilidad de una compañía.", fg='#262626', bg='lightblue')
    l9.config(font=('Comic Sans MS', 15))
    l9.place(x=200, y=230)

    def ven1():

        global ingresar1, ingresar2

        new_window = tk.Toplevel()
        new_window.title('Utilidades por acción ')
        new_window.geometry('470x300+725+215')
        new_window.configure(bg='lightblue')
        new_window.resizable(0,0)
        

        s1=tk.Label(new_window, text="Para resolverlo debemos conocer:", bg='lightblue', fg='black')
        s1.pack(padx=5, pady=10, ipadx=5, ipady=5, fill=tk.X)

        def formula1():
            formula1=float(ingresar1.get())/float(ingresar2.get())
            return var.set(formula1)

        s2=tk.Label(new_window, text="Utilidades disponibles para los accionistas comunes", bg='#378fae', fg='black')
        s2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        ingresar1=tk.Entry(new_window)
        ingresar1.pack(fill=tk.X, padx=5, ipadx=5, ipady=5)

        s3=tk.Label(new_window, text="Número de acciones en circulación de tipo común", bg='#378fae', fg='black')
        s3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        ingresar2=tk.Entry(new_window)
        ingresar2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        botonform1=tk.Button(new_window,text='Resultado', bg='plum', fg='black', command=formula1,  padx=2, pady=2, width=10)
        botonform1.pack(side=tk.RIGHT)
        botonform1.place(x=25, y=202)

        botonform1=tk.Button(new_window,text='Borrar', bg='plum', fg='black', command=limpiar, padx=2, pady=2, width=10)
        botonform1.pack(side=tk.LEFT)
        botonform1.place(x=360, y=202)

        result1=tk.Label(new_window, bg='lightgray', textvariable=var, padx=5, pady=5, width=30)
        result1.pack()

        def cerrar_win():
            new_window.destroy()
            
        botonform1=tk.Button(new_window,text='Cerrar', bg='#ff9aa2', fg='black', command=cerrar_win, padx=2, pady=2, width=10)
        botonform1.pack()
        botonform1.place(x=195, y=250)

    boton1=tk.Button(window, text="calcular", bg='plum', fg='black', command= ven1, padx=5, pady=5, width=30)
    boton1.pack(side=tk.TOP)
    boton1.place(x=350, y=400)

#se crean las diferentes funcines y a todas se les da el metodo destroy
#Destroy sirve para que a la hora de precionar los botones estos cierren la ventana.

def cerrar_win():
    window.destroy()
    return cerrar_win

def menu_win():
    global f1
    f1=Frame(window, width=300, height=500, bg='#378fae')
    f1.place(x=0, y=0)
    #es la pocisión en donde se ubica el rectangulo de nuestro menu.
    
    def bttn(x, y, text, bcolor, fcolor, cmd):
        
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground'] = '#262626' #000d33
        
        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'
            
        myButton1 = Button(f1, text=text,
                        width=42,
                        height=2,
                        bg=fcolor,
                        border=0,
                        fg='#262626', 
                        activeforeground='#262626',
                        activebackground=bcolor,
                        command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)
        #se crean las dos funciones para que los botones puedan abrir y cerrar el menu.

        myButton1.place(x=x, y=y)
        #Es la ubicación de los botones dentro del menu
    
    bttn(0, 80,'H O M E', '#378fae', '#378fae', home)
    bttn(0, 117, 'Presentación', '#378fae', '#378fae',presentacion)
    bttn(0,154,'Rendimiento de la inversión', '#378fae', '#378fae', ren_inversion)
    bttn(0,191,'Rendimiento del capital social', '#378fae', '#378fae', cap_social)
    bttn(0,228,'Utilidades por acción', '#378fae', '#378fae', utilidades)
    bttn(0,265, 'Salir', '#378fae',  '#378fae', cerrar_win)

    #se crean los botones que se almacenaran en menu_win, 
    # además se hace llamado a las fuciones para que estos puedan acceder a los otros apartados.

    def dele():
        f1.destroy()

    global img2 
    img2=ImageTk.PhotoImage(Image.open('close.png'))

    Button(f1, image=img2, command=dele, border=0, activebackground='#378fae',bg='#378fae').place(x=5, y=10)

default_home()

img1=ImageTk.PhotoImage(Image.open('open.png'))
Button(window, command=menu_win, image=img1, border=0,bg='#262626', activebackground='#262626').place(x=5, y=10)

#se crean los botones para desplegar el menu.

window.mainloop()
        