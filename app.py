import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from modele.classe import Classe
from modele.cours import Cours
from modele.eleve import Eleve
from modele.enseigant import Enseignant
from modele.matiere import Matiere

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
posx = 400
posy = 200
root.configure(bg='gray')
root.geometry('{0}x{1}+{2}+{3}'.format(width, height, str(posx), str(posy)))


# MENUS

menubar = Menu(root, tearoff=0)
root.config(menu=menubar)

menuEleve = Menu(menubar, tearoff=0)
menuEleve.add_command(label="Afficher les élèves")
menubar.add_cascade(label="Eleve", menu=menuEleve)


menuCours = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Cours", menu=menuCours)

menuMatiere = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Matiere", menu=menuMatiere)


menuEnseignant = Menu(menubar, tearoff=0)
menuEnseignant.add_command(label="Afficher liste des enseignants")
menubar.add_cascade(label="Enseignant", menu=menuEnseignant)

menuClasse = Menu(menubar, tearoff=0)

menuClasse.add_command(label="Liste d'élèves par classe")
menubar.add_cascade(label="Classe", menu=menuClasse)

menubar.add_command(label="Quitter", command=root.destroy)

### LES POP UP DU MENU ELEVE ###

# Pop up pour ajouter un élève
def popAjoutEleve():
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
    top.bouton_valider = tk.Button(top, text="Valider", command=Eleve.ajoutNewEleve(top.nom.get(), top.prenom.get(), top.idclasse.get()))
    top.bouton_valider.pack()


menuEleve.add_command(label="Ajout d'un élève", command=popAjoutEleve)

# Pop up pour associer un élève à une classe

def AssocierApprenantClasse():
    a = Toplevel(menuEleve)
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
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuEleve.add_command(label="Association d'un élève à une classe", command=AssocierApprenantClasse)


# Pop up pour supprimer un élève
def SupprimerApprenant():
    a = Toplevel(menuEleve)
    a.title("Supprimer un élève")
    a.geometry("300x200")
    a.config(bg="gray")
    a.label_id = tk.Label(a, text="ID :")
    a.label_id.pack()
    a.id = tk.Entry(a)
    a.id.pack()
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuEleve.add_command(label="Suppresion d'un élève", command= SupprimerApprenant)

### LES POP UPS DU MENU ENSEIGNANT ###

# Pop up pour ajouter un enseignant

def AjouterEnseignant():
    a = Toplevel(menuEnseignant)
    a.title("Ajouter un enseignant")
    a.geometry("300x200")
    a.config(bg="gray")
    a.label_nom = tk.Label(a, text="Nom :")
    a.label_nom.pack()
    a.nom = tk.Entry(a)
    a.nom.pack()
    a.label_prenom = tk.Label(a, text="Prenom :")
    a.label_prenom.pack()
    a.prenom = tk.Entry(a)
    a.prenom.pack()
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuEnseignant.add_command(label="Ajout d'un enseignant", command=AjouterEnseignant)

# Pop up pour associer un enseignant à une matière.

def AssocierEnseignantMatiere():
    a = Toplevel(menuEnseignant)   
    a.title("Associer un enseignant à une matière")
    a.geometry("300x200")
    a.config(bg="gray")
    a.label_id_enseignant = tk.Label(a, text="ID enseignant :")
    a.label_id_enseignant.pack()
    a.id_enseignant = tk.Entry(a)
    a.id_enseignant.pack()
    a.label_id_matiere = tk.Label(a, text="ID matière :")
    a.label_id_matiere.pack()
    a.id_matiere = tk.Entry(a)
    a.id_matiere.pack()
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuEnseignant.add_command(label="Association d'un enseignant a une matière", command=AssocierEnseignantMatiere)

# Pop up pour supprimer un professeur

def SupprimerEnseignant():
    a = Toplevel(menuEnseignant)  
    a.title("Supprimer un enseignant")
    a.geometry("300x200")
    a.config(bg="gray")
    a.label_id = tk.Label(a, text="ID :")
    a.label_id.pack()
    a.id = tk.Entry(a)
    a.id.pack()
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuEnseignant.add_command(label="Supprimer un enseignant", command=SupprimerEnseignant)

### LES POP UP DU MENU MATIERE ###

# Pop up pour ajouter une matière

def AjouterMatiere():
    a = Toplevel(menuMatiere) 
    a.title("Ajouter une matière")
    a.geometry("300x200")
    a.config(bg="gray")
    a.label_nom = tk.Label(a, text="Nom :")
    a.label_nom.pack()
    a.nom = tk.Entry(a)
    a.nom.pack()
    a.label_id_enseignant = tk.Label(a, text="ID enseignant :")
    a.label_id_enseignant.pack()
    a.id_enseignant = tk.Entry(a)
    a.id_enseignant.pack()
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuMatiere.add_command(label="Ajouter une matière", command=AjouterMatiere)

# Pop up pour supprimer une matière

def SupprimerMatiere():     
    a = Toplevel(menuMatiere) 
    a.title("Supprimer une matière")
    a.geometry("300x200")
    a.config(bg="gray")
    a.label_id = tk.Label(a, text="ID :")
    a.label_id.pack()
    a.id = tk.Entry(a)
    a.id.pack()
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuMatiere.add_command(label="Supprimer une matière", command=SupprimerMatiere)

### LES POP UP DU MENU COURS ###

# Pop up pour ajouter un cours
def AjouterCours():
    a = Toplevel(menuCours)    
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
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuCours.add_command(label="Ajout d'un cours", command=AjouterCours)

# Pop up pour modifier un cours
def ModifierCours():
    a = Toplevel(menuCours)   
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
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuCours.add_command(label="Modifier un cours", command=ModifierCours)

# Pop up pour supprimer un cours

def SupprimerCours():
    a = Toplevel(menuCours)
    a.title("Supprimer un cours")
    a.geometry("300x200")
    a.config(bg="gray")
    a.label_id = tk.Label(a, text="ID :")
    a.label_id.pack()
    a.id = tk.Entry(a)
    a.id.pack()
    a.bouton_valider = tk.Button(a, text="Valider", command=valider)
    a.bouton_valider.pack()

menuCours.add_command(label="Supprimer un cours", command=SupprimerCours)

root.mainloop()