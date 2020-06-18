from tkinter import *
fenetre = Tk()
champ_label = Label(fenetre, text="c'est ici que ça se passe",fg="green")
champ_label.pack()
bouton=Button(fenetre,text="Quitter", command=fenetre.destroy)
bouton.pack()
"fenetre.mainloop()"
cv=Canvas(fenetre,width=1250,height=400,background="white")
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
