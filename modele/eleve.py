import sqlite3

class Eleve:    

    def __init__(self, nomApprenant, prenomApprenant):
        self.__nomApprenant = nomApprenant
        self.__prenomApprenant = prenomApprenant

    def __init__(self, nomApprenant, prenomApprenant, idEleve, idClasse):
        self.__nomApprenant = nomApprenant
        self.__prenomApprenant = prenomApprenant
        self.__idEleve = idEleve
        self.__idClasse = idClasse

    def get_nomApprenant(self):
        return self.__nomApprenant

    def set_nomApprenant(self, nomApprenant):
        self.__nomApprenant = nomApprenant    

    def get_prenomApprenant(self):
        return self.__prenomApprenant

    def set_prenomApprenant(self, prenomApprenant):
        self.__prenomApprenant = prenomApprenant 


    def get_idEleve(self):
        return self.__idEleve

    def set_idEleve(self, idEleve):
        self.__idEleve = idEleve 

    def get_idClasse(self):
        return self.__idClasse

    def set_idClasse(self, idClasse):
        self.__idClasse = idClasse 

    def ajoutNewEleve(nomApprenant, prenomApprenant, idClasse):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        apprenant = [(nomApprenant, prenomApprenant,idClasse),]
        cursorForDB.executemany("INSERT INTO APPRENANT (nomApprenant, prenomApprenant,idClasse) VALUES (?,?,?)",apprenant)
        conn.commit()
        conn.close()

    def deleteEeve(id):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        i = (id,)
        cursorForDB.execute("DELETE FROM APPRENANT WHERE idEleve = ?",i)
        conn.commit()
        conn.close()

    def mofidEleve(idEleve, idClasse, nomApprenant, prenomApprenant):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        apprenant = [(nomApprenant,prenomApprenant,idClasse, idEleve),]
        cursorForDB.executemany("UPDATE APPRENANT SET nomApprenant = ? , prenomApprenant = ?, idClasse= ? WHERE idEleve = ?",apprenant)
        conn.commit()
        conn.close()

    def listEleve():
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        e = (cursorForDB.execute('SELECT * FROM APPRENANT').fetchall())
        conn.commit()
        conn.close()
        print(e[0])
        return e
