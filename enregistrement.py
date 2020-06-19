import mysql.connector

nbmaxfigures=5
mysql=mysql.connector.connect(host="localhost", user="root", passwd="", database="genese")
mycursor=mysql.cursor()

def enregistrement(liste_figures):
    sql="insert into creation(figure_1, figure_2, figure_3, figure_4, figure_5) VALUES (%s,%s,%s,%s,%s)"
    
    val=[(liste_figures)]
    print(val)
    mycursor.executemany(sql,val)

    mysql.commit();

    print("la table creation a ete completee");