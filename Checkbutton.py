from tkinter import*

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismo=IntVar()

def opciones_viaje():

	opciones_escogida=""

	if(playa.get() is 1):
		opciones_escogida+=" playa"

	if(montana.get() is 1):
		opciones_escogida+=" montaña"

	if(turismo.get() is 1):
		opciones_escogida+=" Turismo"

	textofinal.config(text=opciones_escogida)


foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()
Label(frame,text ="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa",variable=playa,onvalue=1,offvalue=0,command=opciones_viaje).pack()
Checkbutton(frame, text="Montaña",variable=montana,onvalue=1,offvalue=0,command=opciones_viaje).pack()
Checkbutton(frame, text="Turismo",variable=turismo,onvalue=1,offvalue=0,command=opciones_viaje).pack()

textofinal=Label(frame)
textofinal.pack()



root.mainloop()