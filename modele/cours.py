class Cours:

    def __init__(self, idCours, jourCours, heureCours):
        self.__idCours = idCours
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
