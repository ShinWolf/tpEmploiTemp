import sqlite3


class Matiere:

    def __init__(self, libelleMatiere):
        self.__libelleMatiere = libelleMatiere

    def get_libelleMatiere(self):
        return self.__libelleMatiere
    def set_libelleMatiere(self, libelleMatiere):
        self.__libelleMatiere = libelleMatiere
    

    def ajoutMatiere(nomMatiere):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        nom = (nomMatiere,)
        cursorForDB.execute("Insert into MATIERE(libelleMatiere) values(?)", nom)
        conn.commit()
        conn.close()

    def delMatiere(nomMatiere):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB =  conn.cursor()
        cursorForDB.execute("DELETE FROM MATIERE WHERE libelleMatiere = (?)", (nomMatiere,))
        conn.commit()
        conn.close()


