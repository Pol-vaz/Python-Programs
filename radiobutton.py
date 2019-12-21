from tkinter import*

root=Tk()

opcion= IntVar()

def imprimir():

	#print(opcion.get())

	if opcion.get() is 1:

		etiqueta.config(text="Has elegido masculino")

	elif opcion.get() is 2:

		etiqueta.config(text="Has elegido femenino")

	else:

		etiqueta.config(text="Lo que elegirían los amigos de Fran*")

Label(root, text="Género: ").pack()

Radiobutton(root, text="Masculino",variable=opcion, value= 1,command=imprimir).pack()

Radiobutton(root, text="Femenino",variable=opcion, value= 2,command=imprimir).pack()

Radiobutton(root, text="No binario",variable=opcion, value= 3,command=imprimir).pack()


etiqueta =Label(root)
etiqueta.pack()



root.mainloop()
