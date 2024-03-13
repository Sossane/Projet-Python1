"""'''
    page de test qui permets de faire une recuperations de tout les données qui se trouve sur le
    fichier csv  importons le package csv et json afin de formater l'affichage pour que çà 
    soit plus clair lors de l'execution
    des commandes
'''


import csv 
import json 
Donnees_tab = [] 
with open ('Echantillons_Donnees_python.csv') as dp:
    data = csv.DictReader(dp, delimiter=" ")

    for d in data:

        Donnees_tab.append(d)

    print (json.dumps(Donnees_tab, indent=4))
    print(Donnees_tab)




    def numero(numero):
     for i in numero:
        list_valide = []
        if len(numero) == 7  and numero.isalnum() :
            #list_valide.append(numero)
            return True
        else:
            return False
        

run = numero("1234567")
print (run)"""

"""from datetime import datetime
from datetime import datetime

def datenaissance_valide(datenaiss):
    # Vérification du format de l'année
    format_annee = "%Y" if len(datenaiss.split("/")[-1]) == 4 else '%y'

    # Tentative de conversion de la date
    try:
        DATE_FORMAT = datetime.strptime(datenaiss, f"%d/%m/{format_annee}")
    except ValueError:
        return False  # La date n'est pas dans le bon format

    # Vérification de la date de naissance
    jour = int(datenaiss.split("/")[0])
    mois = int(datenaiss.split("/")[1])

    if jour <= 31 and mois <= 12:
        # La date est valide
        return True
    else:
        # La date est invalide
        return False

# Exemples d'utilisation
print(datenaissance_valide("31/12/2000"))  # True
print(datenaissance_valide("32/12/2000"))  # False
print(datenaissance_valide("31/13/2000"))  # False
"""

"""def datenaissance_valide(datenaiss):
        format_annee = "%Y" if len(datenaiss.split("/")[-1]) == 4 else '%y'
        DATE_FORMAT =datetime.strptime(datenaiss, f"%d/%m/{format_annee}")
        format = DATE_FORMAT.strftime(f"%d/%m/{format_annee}")

    # Vérification de la date de naissance
        #try:
        if format == datenaiss:
            return True
        #except ValueError:
         #   print(ValueError)
        else:
            return False
dt = '12/12/12'
print(datenaissance_valide(dt))"""

import re

"""def classe_valide(classe):
    CLASS_FORMAT = "[3-6]e[A-D]"
    if not re.match(CLASS_FORMAT, classe):
        return False 
    else:
        return True    

# Exemple d'utilisation
cl = '5eA'
print(classe_valide(cl))
"""
"""def classe_valide(classe):
    CLASS_FORMAT = "[3-6]e[A-D]"
    try:
        if not re.match(CLASS_FORMAT, classe):
            raise ValueError(f"Format de classe invalide : {classe}")
    except ValueError as e:
        print(f"Erreur : {e}")
        return False
    return True

cl = '5e  A'
print(classe_valide(cl))"""
"""def verifier_ligne(ligne):
    line_valide = True
    raison_invalide = None
    print(ligne)
    line_valide=nom_valide(ligne['Nom'])
    line_valide=numero_valide(ligne['Numero'])
    line_valide=prenom_valide(ligne['Prénom'])
    line_valide=datenaissance_valide(ligne['Date de naissance'])
    line_valide=classe_valide(ligne['Classe'])
    line_valide=note_valide(ligne['Note'])
    return line_valide
    # Vérification du nom
    if not nom_valide(ligne['Nom']):
        line_valide = False
        raison_invalide = "Nom invalide"

    # Vérification des autres champs...

    if not line_valide:
        ligne['Raison'] = raison_invalide
        donnees_invalides.append(ligne)
    """

"""def classe_valide(classe):
    CLASS_FORMAT = "[3-6]e[A-D]"
    try:
        if not re.match(CLASS_FORMAT, classe):
            raise ValueError(f"Format de classe invalide : {classe}")
    except ValueError as e:
        print(f"Erreur : {e}")
        return False
    return True"""

"""def classe_valide(classe):
    CLASS_FORMAT = "[3-6]e[A-D]"
    if not re.match(CLASS_FORMAT, classe):    
        return False 
    else:

        return True    

# Exemple d'utilisation
cl = '5emA'
print(classe_valide(cl))"""

"""def classe_valide(classe):
  
  Convertit la classe fournie au format "3emeA".

  Args:
      classe (str): La chaîne représentant la classe (ex: "3", "4e A", "6èmeB").

  Returns:
      str: La classe au format "3emeA" ou une chaîne vide si la classe est invalide.
  

  niveau = ["3", "4", "5", "6"]
  categorie = ["A", "B", "C", "D"]

  # Vérification du niveau
  if classe[0] not in niveau:
    return "classe invalide", False

  # Vérification de la catégorie et formatage
  if classe[-1].upper() in categorie:
    return classe[0] + "em" + classe[-1].upper()
  else:
    return "Classe Invalide", False

# Exemples d'utilisation
print(classe_valide("4e Aç"))  # "" (Invalid category)
print(classe_valide("6èmeB"))  # "6emeB"
print(classe_valide("Tle D"))  # "TleD"
print(classe_valide("123"))  # "" (Invalid level)"""


"""cl = '5iemeA' #True
cl1 = '6em  A' #True
cl2 = 'Tle 2' #False
cl3 = '4emB' #True
cl4 = '5ieme F' #False
print(classe_valide(cl4)) """    
"""def classe_valide(classe):
  if len(classe) < 2:
    return False  # Gère les chaînes vides ou à caractère unique

  try:
    niveau = int(classe[0])
  except ValueError:
    print("Premier caractère invalide : Doit être un chiffre.")  # Déclencher une exception
    
  # Valider le niveau (3 à 6) et le dernier caractère (A, B, C ou D)
  if niveau not in [3, 4, 5, 6] or classe[-1] not in ["A", "B", "C", "D"]:
    return False

  return True  # La classe est valide
""
cl = '5iemeA' #True
cl1 = '6em  A' #True
cl2 = 'Tle 2' #False
cl3 = '4emB' #True
cl4 = '5ieme F' #False
print(classe_valide(cl2))  

def classe_valide(classe):
    niveau = classe[0]
    if niveau not in [3,4,5,6] or classe[-1] not in ["A", "B" , "C","D"]:
        return False
    else :
        return True """

"""import csv

try:
  # Ouvrir le fichier CSV en lecture
  with open("Echantillons_Donnees_python.csv", "r", newline="") as csvfile:

      # Créer un lecteur CSV
      reader = csv.reader(csvfile, delimiter=",")

      # Sauter la ligne d'en-tête
      next(reader, None)

      # Parcourir chaque ligne du fichier
      for row in reader:

          # Formater la date de naissance
          # Convertir la date de naissance au format JJ/MM/AAAA
          try:
              date_naissance = row[4].split("/")
              date_naissance = date_naissance[2] + "/" + date_naissance[1] + "/" + date_naissance[0]
          except IndexError:
              print(f"Ligne {reader.line_num} : Erreur de format - date de naissance manquante")
              continue

          # Nettoyer les espaces inutiles
          # Supprimer les espaces avant et après chaque cellule
          row = [cell.strip() for cell in row]

          # Séparer les matières et les notes
          # Gérer les lignes avec des données manquantes
          try:
              matieres = row[6].split("#")
              notes = row[7].split("|")
          except IndexError:
              print(f"Ligne {reader.line_num} : Erreur d'index - données incomplètes")
              matieres = []
              notes = []

          # Formater la ligne
          ligne_formatee = f"{row[0]},{row[1]},{row[2]},{row[3]},{date_naissance},{row[5]},{'#'.join(matieres)},{'|'.join(notes)}\n"

          # Écrire la ligne formatée dans un nouveau fichier
          with open("data_formatee.csv", "a", newline="") as csvfile_out:
              csvfile_out.write(ligne_formatee)

except FileNotFoundError:
  print("Fichier d'entrée introuvable. Vérifiez le nom du fichier.")

"""

'''
def verifier_ligne(ligne):
    """"
    Vérifie si la ligne est valide et retourne un booléen.

    Args:
        ligne (dict): Dictionnaire contenant les données de la ligne.

    Returns:
        bool: True si la ligne est valide, False sinon.
    """

    validations = {
        "Date de naissance": date_naissance_format,
       
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
with open("Donnees_python.csv", "r") as fichier:
    reader = csv.DictReader(fichier)    
    # Itération sur les lignes du fichier et validation
    for ligne in reader:
        if verifier_ligne(ligne):
            donnees_valides.append(ligne)
        else:
            donnees_invalides.append(ligne)
        #break

#verifier_ligne(ligne)

print("Données valides:")
print(tabulate.tabulate(donnees_valides))

print("Données invalides:")
print(tabulate.tabulate(donnees_invalides))
'''
"""def classe_valide(classe):

  # Conversion du niveau en chaîne
  try:
    niveau = str(int(classe[0]))
  except ValueError:
    return ""

  # Vérification du format
  if len(classe) < 2 or niveau not in ["3", "4", "5", "6"]:
    return ""

  # Détermination de la catégorie
  categorie = classe[-1].upper()
  if categorie not in ["A", "B", "C", "D"]:
    return ""

  # Formatage de la classe
  classe_formatee = niveau + "em" + categorie

  print(classe_formatee)

classe_valide('6   iem A')"""

from datetime import datetime
import re
import tabulate as tabulate
import csv
from datetime import datetime
import re

def note_valide(note):
    # Vérification des notes
    matieres = note.split("#")
    for matiere in matieres:
        matiere_notes = matiere.split("[")
        if len(matiere_notes) != 2:
            return False
        devoir_notes = matiere_notes[1].split("]")[0]
        examen_note = matiere_notes[1].split("]")[1].split(":")[-1]
        for note in devoir_notes.split("|"):
            if not note.isdigit():
                return False
        if not examen_note.isdigit():
            return False
    return True

def calculer_moyenne(notes_devoir, note_examen):
    total_notes_devoir = sum(notes_devoir)
    moyenne_notes_devoir = total_notes_devoir / len(notes_devoir) if notes_devoir else 0
    moyenne = (moyenne_notes_devoir + 2 * note_examen) / 3
    return moyenne
"""formats_acceptes = [
    "NiveauLettre",  # Ex: 3A
    "NiveauLettreMaj",  # Ex: 3A
    "NiveauemeLettre",  # Ex: 3èmeA
    "NiveauemeLettreMaj",  # Ex: 3èmeA
]

def classe_valide(classe):
    
    Vérifie la classe et retourne la classe formatée si valide, False sinon.

    Args:
        classe (str): La classe à valider.

    Returns:
        str: La classe formatée si valide, False sinon.
   

    for format_accepte in formats_acceptes:
        if format_accepte == "NiveauLettre":
            if len(classe) == 2 and classe[0].isdigit() and classe[1].isalpha():
                return True, f"{classe[0]}ème{classe[1].upper()}"

        elif format_accepte == "NiveauLettreMaj":
            if len(classe) == 2 and classe[0].isdigit() and classe[1].isalpha():
                return True, f"{classe[0]}ème{classe[1]}"

        elif format_accepte == "NiveauemeLettre":
            if len(classe) >= 4 and classe[0].isdigit() and classe[2].isalpha() and classe[1:2] == "ème":
                return True, f"{classe[0]}{classe[2].upper()}"

        elif format_accepte == "NiveauemeLettreMaj":
            if len(classe) >= 4 and classe[0].isdigit() and classe[2].isalpha() and classe[1:2] == "ème":
                return True, f"{classe[0]}{classe[2]}"

    return False, "Le format de la classe est invalide."

"""
def verifier_ligne(ligne):
    """
    Vérifie si la ligne est valide et retourne un booléen.

    Args:
        ligne (dict): Dictionnaire contenant les données de la ligne.

    Returns:
        bool: True si la ligne est valide, False sinon.
    """

    validations = {
        "Note": note_valide,
        # Ajoutez d'autres validations ici
    }

    for champ, fonction_validation in validations.items():
        try:
            if not fonction_validation(ligne[champ]):
                return False
        except KeyError:
            print(f"Champ invalide : {champ}")
            return False

    return True
            if note_valide(ligne['Note']):
            matieres = ligne['Note'].split("#")
            for matiere in matieres:
                nom_matiere, notes = matiere.split("[")
                notes_devoir = [int(note) for note in notes.split("]")[0].split("|")]
                note_examen = int(notes.split("]")[1].split(":")[-1])
                moyenne = calculer_moyenne(notes_devoir, note_examen)
                print(f"Matière : {nom_matiere}")
                print(f"Notes de devoir : {notes_devoir}")
                print(f"Note d'examen : {note_examen}")
                print(f"Moyenne : {moyenne}")
                print()  # Ajouter une ligne vide pour séparer les matières
            else:
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

# Affichage des résultats
print("**Données valides:**")
print((donnees_valides))

print("**Données invalides:**")
print((donnees_invalides))
