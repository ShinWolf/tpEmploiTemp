class Matiere:

    def __init__(self, libelleMatiere):
        self.__libelleMatiere = libelleMatiere

    def get_libelleMatiere(self):
        return self.__libelleMatiere
    def set_libelleMatiere(self, libelleMatiere):
        self.__libelleMatiere = libelleMatiere

    def ajoutMatiere(self, nomMatiere):
        m =  Matiere(nomMatiere)

    def delMatiere(self, nomMatiere):
        del nomMatiere
