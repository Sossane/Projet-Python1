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
    """
    Vérifie si la classe est au format Niveau"eme"Categorie (ex: 3emeA).

    Args:
        classe (str): La classe à valider.

    Returns:
        str: La classe formatée si valide, False sinon.
    """

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
        
"""def verifier_ligne(ligne):
    line_valide = True
    print(ligne)
    line_valide=numero_valide(ligne['Numero'])
    line_valide=nom_valide(ligne['Nom'])
    line_valide=prenom_valide(ligne['Prénom'])
    line_valide=datenaissance_valide(ligne['Date de naissance'])
    line_valide=classe_valide(ligne['Classe'])
    line_valide=note_valide(ligne['Note'])
    return line_valide"""
def verifier_ligne(ligne):
    """
    Vérifie si la ligne est valide et retourne un booléen.

    Args:
        ligne (dict): Dictionnaire contenant les données de la ligne.

    Returns:
        bool: True si la ligne est valide, False sinon.
    """

    validations = {
        "Numero": numero_valide,
        "Nom": nom_valide,
        "Prénom": prenom_valide,
        "Date de naissance": datenaissance_valide,
        "Classe": classe_valide,
        "Note": note_valide,
    }

    for champ, fonction_validation in validations.items():
        try:
            if not fonction_validation(ligne[champ]):
                return False
        except KeyError:
            print(f"Champ invalide : {champ}")
            return False

    return True


# Déclaration des variables
donnees_valides = []
donnees_invalides = []

# Traitement du fichier CSV
try:
    with open("Donnees_python.csv", "r") as fichier:
        reader = csv.DictReader(fichier)
        # Itération sur les lignes du fichier et validation
        for ligne in reader:
            if verifier_ligne(ligne):
                donnees_valides.append(ligne)
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

