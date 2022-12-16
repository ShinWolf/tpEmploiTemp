import sqlite3


class Matiere:

    def __init__(self, libelleMatiere):
        self.__libelleMatiere = libelleMatiere

    def get_libelleMatiere(self):
        return self.__libelleMatiere
    def set_libelleMatiere(self, libelleMatiere):
        self.__libelleMatiere = libelleMatiere
    

    def getIdMatWLibelle(pLibelleMatiere):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDb = conn.cursor()
        idMat = cursorForDb.execute("SELECT idMatiere FROM MATIERE where libelleMatiere= (?)",(pLibelleMatiere,))
        conn.commit()
        return idMat

    def ajoutMatiere(self, nomMatiere):
        m =  Matiere(nomMatiere)

    def delMatiere(self, nomMatiere):
        del nomMatiere

print(Matiere.getIdMatWLibelle("POIN"))
