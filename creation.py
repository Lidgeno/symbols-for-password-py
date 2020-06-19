import mysql.connector
mabdd=mysql.connector.connect(host="localhost", user="root", passwd="")
database=mabdd.cursor()
database.execute("CREATE DATABASE genese")
print("la BDD genese a ete creee");

mysql=mysql.connector.connect(host="localhost", user="root", passwd="", database="genese")
mycursor=mysql.cursor()

#toute la table
#Create Table
mycursor.execute('''CREATE TABLE creation(figure_1 VARCHAR(20), figure_2 VARCHAR(20), figure_3 VARCHAR(20), figure_4 VARCHAR(20), figure_5 VARCHAR(20))''')
print("la table creation a ete creee");
