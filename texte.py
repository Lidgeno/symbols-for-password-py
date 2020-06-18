#main
nbmaxfigures = 5
<<<<<<< Updated upstream
=======
decalagemin=50
>>>>>>> Stashed changes
liste_figures=[]
for i in range (0,nbmaxfigures):
    liste_figures.append("NULL")
#main
<<<<<<< Updated upstream


def manuel():
	valider=0
	numero_figure=1
	while(valider!=1 and numero_figure<nbmaxfigures):
		saisie=input("Veuillez saisir votre figure : ")
		if(saisie=="valider"):
			valider=1
		else:
			reconnu=0

			if(saisie == "cercle" or saisie=="carre" or saisie=="triangle"):
				liste_figures[numero_figure]=saisie
				numero_figure += 1
			else:
				print("la figure est inconnue, veuillez reessayer")
			
	if(numero_figure>nbmaxfigures):
		numero_figure=nbmaxfigures
	print("votre saisie est : ")
	for i in range(1,numero_figure):
		print(liste_figures[i])
=======
import figures

def manuel():
    valider=0
    numero_figure=1
    while(valider!=1 and numero_figure<nbmaxfigures):
        saisie=input("Veuillez saisir votre figure : ")
        if(saisie=="valider"):
            valider=1
        else:
            reconnu=0

            if(saisie == "cercle" or saisie=="carre" or saisie=="triangle"):
                liste_figures[numero_figure]=forme=saisie
                saisie=input("Veuillez saisir sa couleur : ")
                if(saisie != "blue"):
                    saisie="black"
                couleur=saisie
                liste_figures[numero_figure]+=" "+saisie
                decalage=(numero_figure-1)*decalagemin*5
                if(forme=="cercle"):
                    figures.cercle(decalage,50,200,couleur)
                if(forme=="carre"):
                    figures.carre(decalage,50,200,couleur)
                if(forme=="triangle"):
                    figures.triangle(decalage,50,200,couleur)
                numero_figure += 1
            else:
                print("la figure est inconnue, veuillez reessayer")
            
    if(numero_figure>nbmaxfigures):
        numero_figure=nbmaxfigures
    print("votre saisie est : ")
    for i in range(1,numero_figure):
        print(liste_figures[i])
>>>>>>> Stashed changes
