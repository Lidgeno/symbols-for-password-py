#main
nbmaxfigures = 5
<<<<<<< Updated upstream
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
=======
liste_figures=[]
espacement=50
for i in range (0,nbmaxfigures):
    liste_figures.append("NULL")
#main
from figures import *
from enregistrement import *

def manuel():
    valider=0
    numero_figure=0
    while(valider!=1 and numero_figure<nbmaxfigures):
        compteur=0
        valeur=-1
        couleur="NULL"
        fr_form=["carre","cercle","triangle"]
        en_form=["square","circle","triangle"]

        saisie_form=input("donne moi une forme : ")
        if(saisie_form=="valider"):
            valider=1
        else:
            if(saisie_form in fr_form):
                print("la forme est en francais")
                lang_form=fr_form
            elif(saisie_form in en_form):
                print("la forme est en anglais")
                lang_form=en_form
            else:
                print("la figure est inconnue, veuillez reessayer")
                lang_form="NULL"
            if(lang_form != "NULL"):
                fr_coul=["noir","violet","bleu","cyan","vert","jaune","orange","rouge","rose","blanc"]
                en_col=["black","purple","blue","cyan","green","yellow","orange","red","pink","white"]
                saisie_coul=input("donne moi une couleur : ")
                if(saisie_coul in en_col):
                    print("la couleur est en anglais")
                    lang_coul=en_col
                elif(saisie_coul in fr_coul):
                    print("la couleur est en francais")
                    lang_coul=fr_coul
                else:
                    couleur="grey"
                    print("la couleur est inconnue")
                    
                if(couleur!="grey"):
                    for coul_tab in lang_coul:
                        if(coul_tab in saisie_coul):
                            valeur=compteur
                        compteur += 1
                    if(valeur!=-1):
                        couleur=en_col[valeur]
                print(couleur)

                compteur=0
                
                for form_tab in lang_form:
                    if(form_tab in saisie_form):
                        valeur=compteur
                    compteur += 1
                forme=fr_form[valeur]
                    
                if(forme=="carre"):
                    carre(espacement*(1+3*numero_figure),50,100,couleur)
                elif(forme=="cercle"):
                    cercle(espacement*(1+3*numero_figure),50,100,couleur)
                else:
                    triangle(espacement*(1+3*numero_figure),50,100,couleur)
                        
                liste_figures[numero_figure]= forme+" "+couleur
                numero_figure += 1
    if(numero_figure>nbmaxfigures):
        numero_figure=nbmaxfigures
    print("votre saisie est : ")
    for i in range(0,numero_figure):
        print(liste_figures[i])

    enregistrement(liste_figures)
>>>>>>> Stashed changes
