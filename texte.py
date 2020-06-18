#main
nbmaxfigures = 5
liste_figures=[]
for i in range (0,nbmaxfigures):
    liste_figures.append("NULL")
#main


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
