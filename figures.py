from tkinter import *
fenetre = Tk()
champ_label = Label(fenetre, text="c'est ici que ça se passe",fg="green")
champ_label.pack()
bouton=Button(fenetre,text="Quitter", command=fenetre.destroy)
bouton.pack()
"fenetre.mainloop()"
cv=Canvas(fenetre,width=1000,height=1000,background="white")
cv.pack()


def cercle(decalx,decaly,long, intern):
    extern=intern
    cv.create_oval(decalx,decaly,decalx+long,decaly+long, fill=intern, outline=extern)

def carre(decalx,decaly,long, intern):
    extern=intern
    cv.create_rectangle(decalx,decaly,decalx+long,decaly+long, fill=intern, outline=extern)

def triangle(decalx,decaly,long, intern):
    extern=intern
    cv.create_polygon(decalx,decaly+long,decalx+(long/2),decaly,decalx+long,decaly+long, fill=intern, outline=extern)
    
carre(50,500,100,"red")
cercle(200,500,100,"green")
triangle(350,500,100,"blue")
