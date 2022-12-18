# # import tkinter as tk

# # class ScheduleGUI:
# #     def __init__(self, root):
# #         self.root = root
# #         root.title("Emploi du temps")

# #         self.days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
# #         self.hours = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']

# #         # Créer une grille pour afficher les jours de la semaine et les heures
# #         for i in range(7):
# #             tk.Label(root, text=self.days[i]).grid(row=0, column=i+1)
# #             for j in range(10):
# #                 tk.Label(root, text=self.hours[j]).grid(row=j+1, column=0)

# #         # Créer des widgets de texte pour afficher l'emploi du temps
# #         self.schedule_widgets = []
# #         for i in range(7):
# #             column = []
# #             for j in range(10):
# #                 widget = tk.Text(root, width=20, height=3)
# #                 widget.grid(row=j+1, column=i+1)
# #                 column.append(widget)
# #             self.schedule_widgets.append(column)

# # root = tk.Tk()
# # app = ScheduleGUI(root)
# # root.mainloop()

# # import tkinter as tk

# # # Création de la fenêtre principale
# # window = tk.Tk()
# # window.title("Emploi du temps")

# # # Création de la base de données de l'emploi du temps (un dictionnaire Python)
# # emploi_du_temps = {
# #     "Lundi": "Travail",
# #     "Mardi": "Cours de gym",
# #     "Mercredi": "Réunion de travail",
# #     "Jeudi": "Cours de cuisine",
# #     "Vendredi": "Temps libre",
# #     "Samedi": "Promenade en forêt",
# #     "Dimanche": "Brunch avec amis"
# # }

# # # Création d'une étiquette et d'une entrée de texte pour afficher et modifier les entrées de l'emploi du temps
# # label_jour = tk.Label(text="Jour :")
# # label_jour.grid(row=0, column=0)
# # entry_jour = tk.Entry()
# # entry_jour.grid(row=0, column=1)

# # label_activite = tk.Label(text="Activité :")
# # label_activite.grid(row=1, column=0)
# # entry_activite = tk.Entry()
# # entry_activite.grid(row=1, column=1)

# # # Création d'un bouton pour ajouter une entrée à l'emploi du temps
# # def ajouter_activite():
# #     jour = entry_jour.get()
# #     activite = entry_activite.get()
# #     emploi_du_temps[jour] = activite
# #     afficher_emploi_du_temps()

# # bouton_ajouter = tk.Button(text="Ajouter", command=ajouter_activite)
# # bouton_ajouter.grid(row=2, column=0)

# # # Création d'un bouton pour supprimer une entrée de l'emploi du temps
# # def supprimer_activite():
# #     jour = entry_jour.get()
# #     if jour in emploi_du_temps:
# #         del emploi_du_temps[jour]
# #     afficher_emploi_du_temps()

# # bouton_supprimer = tk.Button(text="Supprimer", command=supprimer_activite)
# # bouton_supprimer.grid(row=2, column=1)

# # # Création d'une zone de texte pour afficher l'emploi du temps
# # text_emploi_du_temps = tk.Text()
# # text_emploi_du_temps.grid(row=3, column=0, columnspan=2)

# # # Fonction pour afficher l'emploi du temps dans la zone de texte
# # def afficher_emploi_du_temps():
# #     text_emploi_du_temps.delete("1.0", tk.END)
# #     for jour, activite in emploi_du_temps.items():
# #         text_emploi_du_temps.insert(tk.END, f"{jour}: {activite}\n")

# # # Afficher l'emploi du temps initial
# # afficher_emploi_du_temps()

# # # Exécuter la boucle principale de tkinter pour afficher l'interface graphique
# # window.mainloop()
# import tkinter as tk

# # Création de la fenêtre principale
# window = tk.Tk()
# window.title("Emploi du temps")

# # Création de la base de données de l'emploi du temps (un dictionnaire Python)
# emploi_du_temps = {
#     "Lundi": {},
#     "Mardi": {},
#     "Mercredi": {},
#     "Jeudi": {},
#     "Vendredi": {},
#     "Samedi": {},
#     "Dimanche": {}
# }

# # Création d'une étiquette et d'une entrée de texte pour sélectionner le jour
# label_jour = tk.Label(text="Jour :")
# label_jour.grid(row=0, column=0)
# entry_jour = tk.Entry()
# entry_jour.grid(row=0, column=1)

# # Création d'une étiquette et d'une entrée de texte pour sélectionner l'heure
# label_heure = tk.Label(text="Heure :")
# label_heure.grid(row=1, column=0)
# entry_heure = tk.Entry()
# entry_heure.grid(row=1, column=1)

# # Création d'une étiquette et d'une entrée de texte pour entrer la matière
# label_matiere = tk.Label(text="Matière :")
# label_matiere.grid(row=2, column=0)
# entry_matiere = tk.Entry()
# entry_matiere.grid(row=2, column=1)

# # Création d'un bouton pour ajouter une matière à l'emploi du temps
# def ajouter_matiere():
#     jour = entry_jour.get()
#     heure = entry_heure.get()
#     matiere = entry_matiere.get()
#     emploi_du_temps[jour][heure] = matiere
#     afficher_emploi_du_temps()

# bouton_ajouter = tk.Button(text="Ajouter", command=ajouter_matiere)
# bouton_ajouter.grid(row=3, column=0)

# # Création d'une zone de texte pour afficher l'emploi du temps
# text_emploi_du_temps = tk.Text()
# text_emploi_du_temps.grid(row=4, column=0, columnspan=2)

# # Fonction pour afficher l'emploi du temps dans la zone de texte
# def afficher_emploi_du_temps():
#     text_emploi_du_temps.delete("1.0", tk.END)
#     for jour, horaire in emploi_du_temps.items():
#         text_emploi_du_temps.insert(tk.END, f"{jour}:\n")
#         for heure, matiere in horaire.items():
#             text_emploi_du_temps.insert(tk.END, f"  {heure}: {matiere}\n")

# # Afficher l'emploi du temps initial (vide)
# afficher_emploi_du_temps()

# # Exécuter la boucle principale de tkinter pour afficher l'interface graphique
# window.mainloop()
import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()

# Création de la liste de données à afficher
liste_donnees = [('John', 25), ('Alice', 32), ('Bob', 41), ('Eve', 29)]

def afficher_donnees():
    # Récupération de la valeur saisie dans la zone de texte
    valeur_saisie = zone_texte.get()

    # Filtrage de la liste de données en fonction de la valeur saisie
    donnees_filtrees = [(nom, age) for nom, age in liste_donnees if nom == valeur_saisie]

    # Création de la boîte de dialogue
    boite_dialogue = tk.Toplevel()
    boite_dialogue.title('Données filtrées')

    # Création de la zone de texte pour afficher les données filtrées
    zone_texte_donnees = tk.Text(boite_dialogue)

    # Ajout de chaque élément de la liste filtrée à la zone de texte
    for nom, age in donnees_filtrees:
        zone_texte_donnees.insert(tk.END, f'{nom}: {age}\n')

    # Affichage de la zone de texte dans la boîte de dialogue
    zone_texte_donnees.pack()

# Création de la zone de texte pour saisir une valeur
zone_texte = tk.Entry(fenetre)
zone_texte.pack()

# Création du bouton pour afficher les données filtrées
bouton_afficher = tk.Button(fenetre, text='Afficher les données', command=afficher_donnees)
bouton_afficher.pack()

# Affichage de la fenêtre principale
fenetre.mainloop()

