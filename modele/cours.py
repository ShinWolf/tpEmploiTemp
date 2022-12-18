import sqlite3

class Cours:

    def __init__(self, jourCours, heureCours):
        self.__jourCours = jourCours
        self.__heureCours = heureCours


    def get_jourCours(self):
        return self.__jourCours

    def set_jourCours(self, jourCours):
        self.__jourCours = jourCours    

    def get_heureCours(self):
        return self.__heureCours

    def set_heureCours(self, heureCours):
        self.__heureCours = heureCours 

    def ajoutNewCours(jourCours, heureCours, idClasse, idEnseignant, idMatiere):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        cour = [(jourCours, heureCours, idClasse, idEnseignant, idMatiere),]
        cursorForDB.executemany("INSERT INTO COURS (jourCours, HeureCours,k_idClasse, k_idEnseignant,k_idMatiere) VALUES (?,?,?,?,?)",cour)
        conn.commit()
        conn.close()

    def deleteCours(id):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        i = (id,)
        cursorForDB.execute("DELETE FROM COURS WHERE idCours=?",i)
        conn.commit()
        conn.close()

    def mofidCours(idCours, jourCours, heureCour, idClasse, idEnseignant, idMatiere ):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        cour = [(jourCours,heureCour,idClasse, idEnseignant,idMatiere,idCours),]
        cursorForDB.executemany("UPDATE COURS SET jourCours = ? , heureCours = ?, k_idClasse= ?, k_idEnseignant = ?, k_idMatiere =?  WHERE idCours = ?",cour)
        conn.commit()
        conn.close()

    def listeCoursClass(idClasse):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        lesCours = cursorForDB.execute("SELECT jourCours, heureCours, k_idClasse FROM COURS WHERE k_idClasse = ?", (idClasse,))
        conn.commit()
        return lesCours