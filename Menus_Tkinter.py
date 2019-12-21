from tkinter import*

root=Tk()

barramenu=Menu(root)

root.config( menu=barramenu)

archivoMenu=Menu(barramenu)

archivoEdicion=Menu(barramenu)

archivoHerramientas=Menu(barramenu)

archivoAyuda=Menu(barramenu)

barramenu.add_cascade(Label="Archivo", menu=archivoMenu)
barramenu.add_cascade(Label="Edición", menu=archivoEdicion)
barramenu.add_cascade(Label="Herramientas", menu=archivoHerramientas)
barramenu.add_cascade(Label="Ayuda", menu=archivoAyuda)

root.mainloop()