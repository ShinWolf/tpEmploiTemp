import sqlite3

class Eleve:    

    def __init__(self, nomApprenant, prenomApprenant):
        self.__nomApprenant = nomApprenant
        self.__prenomApprenant = prenomApprenant

    def get_nomApprenant(self):
        return self.__nomApprenant

    def set_nomApprenant(self, nomApprenant):
        self.__nomApprenant = nomApprenant    

    def get_prenomApprenant(self):
        return self.__prenomApprenant

    def set_prenomApprenant(self, prenomApprenant):
        self.__prenomApprenant = prenomApprenant 

    def ajoutNewEleve():
        e = Eleve("","")
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        e.set_nomApprenant("Ansart")
        e.set_prenomApprenant("Emelyne")
        apprenant = [(e.get_nomApprenant(),e.get_prenomApprenant(),3),]
        cursorForDB.executemany("INSERT INTO APPRENANT (nomApprenant, prenomApprenant,idClasse) VALUES (?,?,?)",apprenant)
        conn.commit()
        conn.close()

    def deleteEeve(id):
        e = Eleve("","")
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        i = (id,)
        cursorForDB.execute("DELETE FROM APPRENANT WHERE idEleve = ?",i)
        conn.commit()
        conn.close()

Eleve.deleteEeve(32)


        