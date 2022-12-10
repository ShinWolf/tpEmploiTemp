import sqlite3
from modele.matiere import Matiere

m1 = Matiere('JEUX')
print(m1.get_libelleMatiere())

conn = sqlite3.connect('tp2bdd.db')
cursorForDB = conn.cursor()
nom = (m1.get_libelleMatiere(),)
cursorForDB.execute("Insert into MATIERE(libelleMatiere) values(?)", nom)
conn.commit()
print('Envoyer')
conn.close()