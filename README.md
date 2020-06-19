# yung_devoir_homework
School project, where the user is asked to select a few figures to put in a Database
most of the code is going to be written in french, you may ask or use translators while reading forward

Bonjour et bienvenue sur notre projet,
il a pour but de nous faire adopter certains outils de travail tels que github pour nous apprendre à être de meilleurs codeurs/ingénieurs
nous espérons que l'objectif sera atteint. :|

- il y a un main qui gère plusieurs modules
- le module d'envoi à la base de données (BDD) ; enregistrement
- le module de saisie textuelle des figures sélectionnées ; texte
- le module qui représente les figures dans une fenêtre avec tkinter ; figures

optionnel:
malheureusement
le module d'interface qui aurait permis à l'utilisateur de dessiner sa propre figure est encore en phase de développement

comment cela fonctionne:

---->> sur votre localhost (sinon, modifier les fichiers enregistrement et creation), le fichier creation quand run va créer une nouvelle base de données "genese" avec une nouvelle table "creation". Cette table est constituée de 5 champs pour 5 figures.

----->> si votre localhost a déjà la BDD et la table, (c'est à dire lorsque creation.py s'est correctement executé),
vous pouvez maintenant lancer main.py autant de fois que vous le voulez.

main.py lance le module de texte.py "manuel()"
ce module demande à l'utilisateur la forme de la figure et lui redemande si la forme n'est pas reconnue puis il demande la couleur de la figure si la couleur n'est pas reconnue, la forme sera grise par défaut. le programme va demander jusqu'à 5 formes à l'utilisateur. celui-ci pourra arrêter en écrivant "valider" à la place de la forme indiquée.
les formes utilisables sont "carre", "cercle" et "triangle", l'anglais est reconnu.
les couleurs utilisables sont au nombre de 10, l'anglais est également reconnu.

Ensuite la fenêtre apparaît avec les figures tracées et les données sont envoyées dans la base de données.

Nous avons donc bien respecté les consignes avec 3-4 fonctionnalités, en ayant utilisé une BDD et TKinter.
Nous voulions aller plus loin dans le projet infortunément, par manque d'effectifs et avec plusieurs bugs irrésolus, nous avons décidé de ne pas ajouter un dernier module d'interface. L'utilisateur pouvait tracer et changer les couleurs de ses traits mais nous ne pouvons pas encore traiter ces informations.

Nous espérons que notre projet vous a plu et que nous allons résoudre ce dernier problème.

Passez une bonne journée - keep coding !
