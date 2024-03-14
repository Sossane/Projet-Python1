'''
    Cette page nous permettra de recuperer les données dans l'echantillon de données, 
    puis vérifier si les données sont valides,
    ensuite stocker les données valides.
'''

# Importation des modules
import csv
from datetime import datetime
import re
import tabulate as tabulate

def numero_valide(numero):
    # Vérification du numéro
    if not numero.isalnum() or len(numero) != 7:
        return  False
    else:
        return  True


def nom_valide(nom):
    # Vérification du prénom
    if not nom.isalpha() or len(nom) < 2:
        return "nom invalide" , False
    else:
        return "nom valide" ,True  


def prenom_valide(prenom):
    # Vérification du prénom
    if not prenom.isalpha() or len(prenom) < 3:
        return "prenom invalide" , False
    else:
        return "prenom valide" ,True  


def datenaissance_valide(date_naissance):

    # Conversion des séparateurs (remplace tous les caractères non numériques par /)
    date_naissance = re.sub(r"[^\d]", "/", date_naissance)
    # Vérification du format (JJ/MM/AAAA ou JJ/MM/AA)
    if len(date_naissance) not in [8, 10] or not re.match(r"\d{2}/\d{2}/\d{2,4}", date_naissance):
        return False

    # Conversion des parties de la date
    jour = int(date_naissance.split("/")[0])
    mois = int(date_naissance.split("/")[1])

    # Vérification de l'année et conversion si nécessaire
    if len(date_naissance) == 8:
        annee = int(date_naissance.split("/")[2])
    elif len(date_naissance) == 10:
        annee = int(date_naissance.split("/")[2]) + 2000
    else:
        return False

    # Vérification de la validité de la date
    if not 1 <= jour <= 31 or not 1 <= mois <= 12:
        return False

    # Gestion des années bissextiles
    if mois == 2 and jour == 29:
        if not datetime.is_leap_year(annee):
            return False

    # Retourne la date formatée
    return f"{jour:02}/{mois:02}/{annee}"


def classe_valide(classe):
    classe = classe.replace(" ", "")
    classe = classe.strip()
    try:
        # Conversion du niveau en chaîne
        niveau = str(int(classe[0]))
    except ValueError:
        return False

    # Vérification du format
    if len(classe) < 2 or niveau not in ["3", "4", "5", "6"]:
        return False

    # Détermination de la catégorie
    categorie = classe[-1].upper()
    if categorie not in ["A", "B", "C", "D"]:
        return False

    # Formatage de la classe
    classe_formatee = niveau + "eme" + categorie
    return classe_formatee


def note_valide(note):
    # Vérification des notes
        notes = note.split("#")
        for matiere in notes:
            matiere_notes = matiere.split("[")
            if len(matiere_notes) != 2:
                return False
            else:
                return True
        devoir_notes = matiere_notes[1].split("]")[0]
        examen_note = matiere_notes[1].split("]")[1]
    # Vérification des notes de devoir
        for note in devoir_notes.split("|"):
                if not note.isdigit():
                    return False
                else:
                    return True
    # Vérification de la note d'examen
        if not examen_note.isdigit():
            return False
        else:
            return True


def calculer_moyenne(notes_devoir, note_examen):
    total_notes_devoir = sum(notes_devoir)
    moyenne_notes_devoir = total_notes_devoir / len(notes_devoir) if notes_devoir else 0
    moyenne = (moyenne_notes_devoir + 2 * note_examen) / 3
    return moyenne


def verifier_ligne(ligne):
    line_valide = True

    if not numero_valide(ligne['Numero']):
        line_valide = False

    elif not nom_valide(ligne['Nom']):
        line_valide = False

    elif not prenom_valide(ligne['Prénom']):
        line_valide = False

    elif not datenaissance_valide(ligne['Date de naissance']):
        line_valide = False

    elif not classe_valide(ligne['Classe']):
        line_valide = False

    elif not note_valide(ligne['Note']):
        line_valide = False

    """elif not calculer_moyenne(ligne['Moyenne']):
        line_valide = False"""
   
        
    return line_valide


def verifier_ligne1(ligne):
    line_valide = True
    new_line={}
    my_func={
    'Numero':numero_valide,
    'Nom':nom_valide,
    'Prénom':prenom_valide,
    'Date de naissance':datenaissance_valide,
    'Classe':classe_valide,
    'Note':note_valide,
    
}
    
    print(ligne)
    for key,fonct in my_func.items():
        v=ligne[key]
        if(v):
            if(key =="Classe"):
                v=fonct(ligne[key])
            if( fonct(ligne[key])):
                
                new_line.update({key:v})
            else:
                line_valide = False

    # Vérification si la ligne est vide
    if not new_line:
        line_valide = False

    print(new_line)
    print("\n ==============================================================\n")
    return line_valide,new_line


# Déclaration des variables
donnees_valides = []
donnees_invalides = []

# Traitement du fichier CSV
try:
    with open("Donnees_python.csv", "r") as fichier:
        reader = csv.DictReader(fichier)
        # Itération sur les lignes du fichier et validation
        for ligne in reader:
            ver,lg=verifier_ligne1(ligne)
            if ver:
                donnees_valides.append(lg)
            else:
                donnees_invalides.append(ligne)
except FileNotFoundError:
    print("Fichier introuvable")
except Exception as e:
    print(f"Erreur : {e}")

#verifier_ligne(ligne)

print("Données valides:")
print(tabulate.tabulate(donnees_valides))

print("Données invalides:")
print(tabulate.tabulate(donnees_invalides))

def afficher_menu():
    """
    Affiche le menu et gère les interactions avec l'utilisateur.
    """

    while True:
        try:
            print("**Menu de gestion des informations**")
            print("1. Afficher les informations")
            print("2. Afficher une information par son numéro")
            print("3. Afficher les cinq premiers")
            print("4. Ajouter une information")
            print("5. Modifier une information invalide")
            print("0. Quitter")

            choix = input("Choisir une option : ")

            if choix == "1":
                afficher_informations()
            elif choix == "2":
                afficher_information_par_numero()
            elif choix == "3":
                afficher_cinq_premiers()
            elif choix == "4":
                ajouter_information()
            elif choix == "5":
                modifier_information_invalide()
            elif choix == "0":
                break
            else:
                print("Choix invalide")
        except Exception as e:
            print(f"Erreur : {e}")
            print("Une erreur s'est produite. Veuillez réessayer.")

# Les autres fonctions restent les mêmes

def afficher_informations():
    """
    Affiche les informations valides ou invalides selon le choix de l'utilisateur.
    """

    choix = input("Afficher les informations valides (V) ou invalides (I) ? ").upper()
    if choix == "V":
        donnees = donnees_valides
    elif choix == "I":
        donnees = donnees_invalides
    else:
        print("Choix invalide")
        return

    print(tabulate.tabulate(donnees))


def afficher_information_par_numero():
    """
    Affiche une information par son numéro.
    """

    numero = int(input("Saisir le numéro de l'information : "))

    information = trouver_information_par_numero(numero)
    if information is None:
        print(f"Information introuvable avec le numéro {numero}")
        return

    print(tabulate.tabulate([information]))


def afficher_cinq_premiers():
    """
    Affiche les cinq premières informations valides.
    """

    print(tabulate.tabulate(donnees_valides[:5]))


def ajouter_information():
    """
    Ajoute une information et la valide.
    """

    information = {}
    for champ in champs:
        information[champ] = input(f"Saisir {champ} : ")

    if not verifier_ligne(information):
        print("Informations invalides")
        return

    donnees_valides.append(information)

def trouver_information_par_numero(numero):
    """
    Recherche une information par son numéro dans la liste des informations valides ou invalides.

    Args:
        numero (int): Le numéro de l'information à rechercher.

    Returns:
        dict: L'information trouvée ou None si elle n'est pas trouvée.
    """

    for information in donnees_valides + donnees_invalides:
        if information["Numero"] == str(numero):
            return information
    return None


def modifier_information_invalide():
    """
    Modifie une information invalide et la transfère dans la liste des informations valides.
    """

    numero = input("Saisir le numéro de l'information invalide à modifier : ")

    information = trouver_information_par_numero(numero)
    if information is None:
        print(f"Information introuvable avec le numéro {numero}")
        return

    for champ in champs:
        information[champ] = input(f"Modifier {champ} : ")

    if not verifier_ligne(information):
        print("Informations invalides")
        return

    donnees_invalides.remove(information)
    donnees_valides.append(information)



# Déclaration des champs
champs = ["Numero", "Nom", "Prénom", "Date de naissance", "Classe", "Note","Moyenne"]

# Démarrage du menu
afficher_menu()