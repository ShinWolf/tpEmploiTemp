import sqlite3

class Enseignant:

    def __init__(self, nomEnseigant, prenomEnseignant):
        self.__nomEnseignant = nomEnseigant
        self.__prenomEnseignant = prenomEnseignant
        self.__listMatiereAssocie = []

    def get_nomEnseigant(self):
        return self.__nomEnseignant 
    def get_prenomEnseigant(self):
        return self.__prenomEnseignant
    def set_nomEnseignant(self, nom):
        self.__nomEnseignant = nom   
    def set_prenomEnseigant(self, prenom):
        self.__prenomEnseignant = prenom

    def ajoutMatiere(self, matiere):
        self.__listMatiereAssocie.append(matiere)

    def listAllEnseigant():
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        listEnseigants = cursorForDB.execute("SELECT nomEnseignant, prenomEnseignant FROM ENSEIGNANT")
        conn.commit()
        return listEnseigants

    def associerEnseigant(pIdEnseignant, pIdMatiere):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        associer = [(pIdEnseignant, pIdMatiere),]
        cursorForDB.executemany("INSERT INTO MATIERE_ENSEIGNANT (k_idEnseignant, k_idMatiere) VALUES (?,?)",associer)
        conn.commit()
        conn.close()
