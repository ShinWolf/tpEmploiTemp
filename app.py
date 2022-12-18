import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *
from tkinter import messagebox

from modele.eleve import Eleve
from modele.enseigant import Enseignant
from modele.matiere import Matiere
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

menuCours.add_command(label="Ajout d'un cours")
menuCours.add_command(label="Suppression d'un cours")
menuCours.add_command(label="Modification d'un cours")
menubar.add_cascade(label="Cours", menu=menuCours)

menuMatiere = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Matiere", menu=menuMatiere)
menuEnseignant = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Enseignant", menu=menuEnseignant)

menuEnseignant.add_command(label="Afficher liste des enseignants")

menuClasse = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Classe", menu=menuClasse)



menubar.add_command(label="Quitter", command=root.destroy)


# Class pour créer le tableau qui affiche les élèves d'une classe
def afficheListeEleveClasse():
    saisie = zone_texte.get()
    maClasse = Classe.elevesDeClasse(saisie)

    donnees_filtrees = [(nom, prenom, classe) for nom, prenom, classe in maClasse if classe == saisie]

    boite_dialogue = tk.Toplevel()
    boite_dialogue.title('Données filtrées')

    zone_texte_donnees = tk.Text(boite_dialogue)
    for nom, prenom, classe in donnees_filtrees:
        zone_texte_donnees.insert(tk.END, f'{nom} {prenom}: {classe}\n')
    zone_texte_donnees.pack()

def popSaisieNomClasse():
    test = Toplevel(menuClasse)
    test.title("Saisie")
    test.geometry("300x200")
    test.config(bg="gray")
    test.label_prenom = tk.Label(test, text="Nom de la classe :")
    test.label_prenom.pack()
    global zone_texte 
    zone_texte = tk.Entry(test)
    zone_texte.pack()
    bouton_afficher = tk.Button(test, text='Afficher les données', command=afficheListeEleveClasse)
    bouton_afficher.pack()

menuClasse.add_command(label="Liste d'élèves par classe", command=popSaisieNomClasse)
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
class AjouterCours(tk.Toplevel):
    def __init__(a, parent):
        tk.Toplevel.__init__(a, parent)
        a.parent = parent
        a.title("Ajouter un cours")
        a.geometry("300x200")
        a.config(bg="gray")
        a.label_id_matiere = tk.Label(a, text="ID matière :")
        a.label_id_matiere.pack()
        a.id_matiere = tk.Entry(a)
        a.id_matiere.pack()
        a.label_id_apprenant = tk.Label(a, text="ID apprenant :")
        a.label_id_apprenant.pack()
        a.id_apprenant = tk.Entry(a)
        a.id_apprenant.pack()
        a.label_date = tk.Label(a, text="Date :")
        a.label_date.pack()
        a.date = tk.Entry(a)
        a.date.pack()
        a.bouton_valider = tk.Button(a, text="Valider", command=a.valider)
        a.bouton_valider.pack()

# Pop up pour modifier un cours
class ModifierCours(tk.Toplevel):
    def __init__(a, parent):
        tk.Toplevel.__init__(a, parent)
        a.parent = parent
        a.title("Modifier un cours")
        a.geometry("300x200")
        a.config(bg="gray")
        a.label_id = tk.Label(a, text="ID matiere :")
        a.label_id.pack()
        a.id = tk.Entry(a)
        a.id.pack()
        a.label_id_matiere = tk.Label(a, text="jours cours  :")
        a.label_id_matiere.pack()
        a.id_matiere = tk.Entry(a)
        a.id_matiere.pack()
        a.label_id_apprenant = tk.Label(a, text="heure cours :")
        a.label_id_apprenant.pack()
        a.id_apprenant = tk.Entry(a)
        a.id_apprenant.pack()
        a.label_date = tk.Label(a, text="Date :")
        a.label_date.pack()
        a.date = tk.Entry(a)
        a.date.pack()
        a.bouton_valider = tk.Button(a, text="Valider", command=a.valider)
        a.bouton_valider.pack()

# Pop up pour supprimer un cours
class SupprimerCours(tk.Toplevel):
    def __init__(a, parent):
        tk.Toplevel.__init__(a, parent)
        a.parent = parent
        a.title("Supprimer un cours")
        a.geometry("300x200")
        a.config(bg="gray")
        a.label_id = tk.Label(a, text="ID :")
        a.label_id.pack()
        a.id = tk.Entry(a)
        a.id.pack()
        a.bouton_valider = tk.Button(a, text="Valider", command=a.valider)
        a.bouton_valider.pack()


root.mainloop()