import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *
from tkinter import messagebox

from modele.eleve import Eleve
from modele.enseigant import Enseignant
from modele.matiere import Matiere
from modele.cours import Cours
from modele.classe import Classe

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
posx = -10
posy = -10
root.configure(bg='gray')
root.geometry('{0}x{1}+{2}+{3}'.format(width, height, str(posx), str(posy)))


# MENUS

menubar = Menu(root, tearoff=0)
root.config(menu=menubar)

menuEleve = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Eleve", menu=menuEleve)


menuCours = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Cours", menu=menuCours)

menuMatiere = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Matiere", menu=menuMatiere)
menuEnseignant = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Enseignant", menu=menuEnseignant)

menuEnseignant.add_command(label="Afficher liste des enseignants")

menuClasse = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Classe", menu=menuClasse)


def poplistEleveClasse():
    def getValueAffiche():
        Classe.elevesDeClasse(top.classe.get())
    top = Toplevel(menuEleve)
    top.title("Afficher les élèves d'une classe")
    top.geometry("300x200")
    top.config(bg="gray")
    top.label_classe = tk.Label(top, text="classe :")
    top.label_classe.pack()
    top.classe = tk.Entry(top)
    top.classe.pack()
    top.bouton_valider = tk.Button(top, text="Valider", command=getValueAffiche)
    top.bouton_valider.pack()
    

menuClasse.add_command(label="Liste d'élèves par classe",  command=poplistEleveClasse)

menubar.add_command(label="Quitter", command=root.destroy)


# Class pour créer le tableau qui affiche les élèves d'une classe

class Tableau(tk.Frame):
    def __init__(self, parent, result):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.result = result
        self.tableau = ttk.Treeview(self, columns=("ID", "Nom", "Prenom", "Classe"), show="headings")
        self.tableau.heading("ID", text="ID")
        self.tableau.heading("Nom", text="Nom")
        self.tableau.heading("Prenom", text="Prenom")
        self.tableau.heading("Classe", text="Classe")
        self.tableau.pack()
        self.afficher_tableau()

    def afficher_tableau(self):
        for row in self.result:
            self.tableau.insert("", "end", values=row)

### LES POP UP DU MENU ELEVE ###

# Pop up pour ajouter un élève
def popAjoutAppre():
    def getValueAjoutApp():
        Eleve.ajoutNewEleve(top.prenom.get(), top.nom.get(), top.idclasse.get())
    top = Toplevel(menuEleve)
    top.title("Ajouter un élève")
    top.geometry("300x200")
    top.config(bg="gray")
    top.label_nom = tk.Label(top, text="Nom :")
    top.label_nom.pack()
    top.nom = tk.Entry(top)
    top.nom.pack()
    top.label_prenom = tk.Label(top, text="Prénom :")
    top.label_prenom.pack()
    top.prenom = tk.Entry(top)
    top.prenom.pack()
    top.label_idclasse = tk.Label(top, text="idclasse :")
    top.label_idclasse.pack()
    top.idclasse = tk.Entry(top)
    top.idclasse.pack()
    top.bouton_valider = tk.Button(top, text="Valider", command=getValueAjoutApp)
    top.bouton_valider.pack()


def popAfficherEleve():
    def getValueAjoutApp():
        Eleve.listEleve()

def popSupApp():
    def getValueSuppApp():
        Eleve.deleteEeve(top.idclasse.get(), top.nom.get(), top.prenom.get())
    top = Toplevel(menuEleve)
    top.title("Supprimer un élève")
    top.geometry("300x200")
    top.config(bg="gray")
    top.label_nom = tk.Label(top, text="Nom :")
    top.label_nom.pack()
    top.nom = tk.Entry(top)
    top.nom.pack()
    top.label_prenom = tk.Label(top, text="Prénom :")
    top.label_prenom.pack()
    top.prenom = tk.Entry(top)
    top.prenom.pack()
    top.label_idclasse = tk.Label(top, text="idclasse :")
    top.label_idclasse.pack()
    top.idclasse = tk.Entry(top)
    top.idclasse.pack()
    top.bouton_valider = tk.Button(top, text="Valider", command=getValueSuppApp)
    top.bouton_valider.pack()
    

menuEleve.add_command(label="Ajout d'un élève", command=popAjoutAppre)
menuEleve.add_command(label="Supprimer un élève", command=popSupApp)
menuEleve.add_command(label="Afficher la liste d'élève", command=popAfficherEleve)


# Pop up pour associer un élève à une classe
class AssocierApprenantClasse(tk.Toplevel):
    def __init__(a, parent):
        tk.Toplevel.__init__(a, parent)
        a.parent = parent
        a.title("Associer un élève à une classe")
        a.geometry("300x200")
        a.config(bg="gray")
        a.label_id = tk.Label(a, text="ID :")
        a.label_id.pack()
        a.id = tk.Entry(a)
        a.id.pack()
        a.label_classe = tk.Label(a, text="Classe :")
        a.label_classe.pack()
        a.classe = tk.Entry(a)
        a.classe.pack()
        a.bouton_valider = tk.Button(a, text="Valider", command=a.valider)
        a.bouton_valider.pack()


# Pop up pour supprimer un élève
class SupprimerApprenant(tk.Toplevel):
    def __init__(a, parent):
        tk.Toplevel.__init__(a, parent)
        a.parent = parent
        a.title("Supprimer un élève")
        a.geometry("300x200")
        a.config(bg="gray")
        a.label_id = tk.Label(a, text="ID :")
        a.label_id.pack()
        a.id = tk.Entry(a)
        a.id.pack()
        a.bouton_valider = tk.Button(a, text="Valider", command=a.valider)
        a.bouton_valider.pack()

### LES POP UPS DU MENU ENSEIGNANT ###

# Pop up pour ajouter un enseignant
def popAjouterEnseignant():
    def getValAjoutEns():
        Enseignant.ajoutNewEnsei(aE.nom.get(),aE.prenom.get())
    aE = Toplevel(menuEnseignant)
    aE.title("Ajouter un enseignant")
    aE.geometry("300x200")
    aE.config(bg="gray")
    aE.label_nom = tk.Label(aE, text="Nom :")
    aE.label_nom.pack()
    aE.nom = tk.Entry(aE)
    aE.nom.pack()
    aE.label_prenom = tk.Label(aE, text="Prenom :")
    aE.label_prenom.pack()
    aE.prenom = tk.Entry(aE)
    aE.prenom.pack()
    aE.bouton_valider = tk.Button(aE, text="Valider", command=getValAjoutEns)
    aE.bouton_valider.pack()

menuEnseignant.add_command(label="Ajout d'un enseignant", command=popAjouterEnseignant)


# Pop up pour associer un enseignant à une matière.
def popAssocierEnseignantMatiere():
    def getValAssoEnseiMat():
        Enseignant.associerEnseigant(assoE.id_enseignant.get(), assoE.id_matiere.get())
    assoE = Toplevel(menuEnseignant)
    assoE.title("Associer un enseignant à une matière")
    assoE.geometry("300x200")
    assoE.config(bg="gray")
    assoE.label_id_enseignant = tk.Label(assoE, text="ID enseignant :")
    assoE.label_id_enseignant.pack()
    assoE.id_enseignant = tk.Entry(assoE)
    assoE.id_enseignant.pack()
    assoE.label_id_matiere = tk.Label(assoE, text="ID matière :")
    assoE.label_id_matiere.pack()
    assoE.id_matiere = tk.Entry(assoE)
    assoE.id_matiere.pack()
    assoE.bouton_valider = tk.Button(assoE, text="Valider", command=getValAssoEnseiMat)
    assoE.bouton_valider.pack()

menuEnseignant.add_command(label="Association d'un enseignant a une matière", command= popAssocierEnseignantMatiere)


# Pop up pour supprimer un professeur
def popSupprimerEnseignant():
    def getValSupEnsei():
        Enseignant.deleteEnsei(supE.id.get())
    supE = Toplevel(menuEnseignant)
    supE.title("Supprimer un enseignant")
    supE.geometry("300x200")
    supE.config(bg="gray")
    supE.label_id = tk.Label(supE, text="ID :")
    supE.label_id.pack()
    supE.id = tk.Entry(supE)
    supE.id.pack()
    supE.bouton_valider = tk.Button(supE, text="Valider", command=getValSupEnsei)
    supE.bouton_valider.pack()

menuEnseignant.add_command(label="Suppresion d'un enseignant", command=popSupprimerEnseignant)

### LES POP UP DU MENU MATIERE ###

# Pop up pour ajouter une matière
def popAjouterMatiere():
    def getValAjoutMat():
        Matiere.ajoutMatiere(ajoutMat.nom.get())
    ajoutMat = Toplevel(menuMatiere)
    ajoutMat.title("Ajouter une matière")
    ajoutMat.geometry("300x200")
    ajoutMat.config(bg="gray")
    ajoutMat.label_nom = tk.Label(ajoutMat, text="Nom :")
    ajoutMat.label_nom.pack()
    ajoutMat.nom = tk.Entry(ajoutMat)
    ajoutMat.nom.pack()
    ajoutMat.bouton_valider = tk.Button(ajoutMat, text="Valider", command=getValAjoutMat)
    ajoutMat.bouton_valider.pack()

menuMatiere.add_command(label="Ajout d'une matière", command=popAjouterMatiere)


# Pop up pour supprimer une matière
def popSupprimerMatiere():
    def getValSupMat():
        Matiere.delMatiere(supMat.id.get())
    supMat = Toplevel(menuMatiere)
    supMat.title("Supprimer une matière")
    supMat.geometry("300x200")
    supMat.config(bg="gray")
    supMat.label_id = tk.Label(supMat, text="Nom :")
    supMat.label_id.pack()
    supMat.id = tk.Entry(supMat)
    supMat.id.pack()
    supMat.bouton_valider = tk.Button(supMat, text="Valider", command=getValSupMat)
    supMat.bouton_valider.pack()

menuMatiere.add_command(label="Suppression d'une matière", command=popSupprimerMatiere)


### LES POP UP DU MENU COURS ###

# Pop up pour ajouter un cours
def popAjouterCours():
    def getValAjoutMat():
        Cours.ajoutNewCours(ajoutCour.date.get(),ajoutCour.heure.get(),ajoutCour.id_classe.get(),ajoutCour.id_enseignant.get(),ajoutCour.id_matiere.get() )
    ajoutCour = Toplevel(menuCours)
    ajoutCour.title("Ajouter un cours")
    ajoutCour.geometry("300x200")
    ajoutCour.config(bg="gray")
    ajoutCour.label_heure = tk.Label(ajoutCour, text="Heure :")
    ajoutCour.label_heure.pack()
    ajoutCour.heure = tk.Entry(ajoutCour)
    ajoutCour.heure.pack()
    ajoutCour.label_date = tk.Label(ajoutCour, text="Date :")
    ajoutCour.label_date.pack()
    ajoutCour.date = tk.Entry(ajoutCour)
    ajoutCour.date.pack()
    ajoutCour.label_id_matiere = tk.Label(ajoutCour, text="ID matière :")
    ajoutCour.label_id_matiere.pack()
    ajoutCour.id_matiere = tk.Entry(ajoutCour)
    ajoutCour.id_matiere.pack()
    ajoutCour.label_id_enseignant = tk.Label(ajoutCour, text="ID enseignant :")
    ajoutCour.label_id_enseignant.pack()
    ajoutCour.id_enseignant = tk.Entry(ajoutCour)
    ajoutCour.id_enseignant.pack()
    ajoutCour.label_id_classe = tk.Label(ajoutCour, text="ID classe :")
    ajoutCour.label_id_classe.pack()
    ajoutCour.id_classe = tk.Entry(ajoutCour)
    ajoutCour.id_classe.pack()
    ajoutCour.bouton_valider = tk.Button(ajoutCour, text="Valider", command=getValAjoutMat)
    ajoutCour.bouton_valider.pack()

menuCours.add_command(label="Ajout d'un cours", command=popAjouterCours)

# Pop up pour modifier un cours
def popModifCours():
    def getValModCour():
        Cours.mofidCours(modifCour.date.get(),modifCour.heure.get(),modifCour.id_classe.get(),modifCour.id_enseignant.get(),modifCour.id_matiere.get() )
    modifCour = Toplevel(menuCours)
    modifCour.title("Modifier un cours")
    modifCour.geometry("300x200")
    modifCour.config(bg="gray")
    modifCour.label_heure = tk.Label(modifCour, text="Heure :")
    modifCour.label_heure.pack()
    modifCour.heure = tk.Entry(modifCour)
    modifCour.heure.pack()
    modifCour.label_date = tk.Label(modifCour, text="Date :")
    modifCour.label_date.pack()
    modifCour.date = tk.Entry(modifCour)
    modifCour.date.pack()
    modifCour.label_id_matiere = tk.Label(modifCour, text="ID matière :")
    modifCour.label_id_matiere.pack()
    modifCour.id_matiere = tk.Entry(modifCour)
    modifCour.id_matiere.pack()
    modifCour.label_id_enseignant = tk.Label(modifCour, text="ID enseignant :")
    modifCour.label_id_enseignant.pack()
    modifCour.id_enseignant = tk.Entry(modifCour)
    modifCour.id_enseignant.pack()
    modifCour.label_id_classe = tk.Label(modifCour, text="ID classe :")
    modifCour.label_id_classe.pack()
    modifCour.id_classe = tk.Entry(modifCour)
    modifCour.id_classe.pack()
    modifCour.bouton_valider = tk.Button(modifCour, text="Valider", command=getValModCour)
    modifCour.bouton_valider.pack()

menuCours.add_command(label="Modification d'un cours", command= popModifCours)


# Pop up pour supprimer un cours
def popSuppCours():
    def getValSupCour():
        Cours.deleteCours(suppCour.id.get())
    suppCour = Toplevel(menuCours)
    suppCour.title("Supprimer un cours")
    suppCour.geometry("300x200")
    suppCour.config(bg="gray")
    suppCour.label_id = tk.Label(suppCour, text="id :")
    suppCour.label_id.pack()
    suppCour.id = tk.Entry(suppCour)
    suppCour.id.pack()
    suppCour.bouton_valider = tk.Button(suppCour, text="Valider", command=getValSupCour)
    suppCour.bouton_valider.pack()

menuCours.add_command(label="Suppression d'un cours", command=popSuppCours)
root.mainloop()