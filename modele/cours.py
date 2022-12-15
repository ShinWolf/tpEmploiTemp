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

    def ajoutNewCours():
        c = Cours("","")
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        c.set_jourCours("21-10-2019")
        c.set_heureCours("AM")
        cour = [(c.get_jourCours(),c.get_heureCours(),3,1,1),]
        cursorForDB.executemany("INSERT INTO COURS (jourCours, HeureCours,k_idClasse, k_idEnseignant,k_idMatiere) VALUES (?,?,?,?,?)",cour)
        conn.commit()
        conn.close()

    def deleteCours(id):
        c = Cours("","")
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        i = (id,)
        cursorForDB.execute("DELETE FROM COURS WHERE idCours=?",i)
        conn.commit()
        conn.close()
