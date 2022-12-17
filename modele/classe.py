import sqlite3


class Classe:

    def __init__(self, libelleClasse):
        self.__libelleClasse = libelleClasse
        self.listEleveClasse = []

    def elevesDeClasse(libelleClasse):
        conn = sqlite3.connect('tp2bdd.db')
        cursorForDB = conn.cursor()
        listEleveClasse = cursorForDB.execute("SELECT nomApprenant, prenomApprenant, libelleClasse FROM APPRENANT INNER JOIN CLASSE on APPRENANT.idClasse = CLASSE.idClasse WHERE libelleClasse = (?)", (libelleClasse,))
        conn.commit()
        return listEleveClasse
