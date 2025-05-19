# Calcul de la moyenne

print("Ce programme va calculer votre moyenne.\n")

# Fonction qui demande une note à l'utilisateur pour une matière donnée
def demander_note(matiere):
    while True:
        try:
            # Saisie de la note
            note = float(input(f"Entrez la note en {matiere} sur 20 : "))
            # Vérification que la note est dans l'intervalle autorisé
            if 0 <= note <= 20:
                return note
            else:
                print("La note doit être entre 0 et 20.")
        except:
            print("Veuillez entrer un nombre valide.")

# Saisie des informations personnelles
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")

# Saisie des notes dans chaque matière
note1 = demander_note("Français")
note2 = demander_note("Anglais")
note3 = demander_note("Physique")
note4 = demander_note("Mathématiques")
note5 = demander_note("Sport")

# Calcul de la moyenne des 5 notes
moyenne = (note1 + note2 + note3 + note4 + note5) / 5

# Attribution d'une mention selon la moyenne obtenue
if moyenne >= 16:
    mention = "Très bien"
elif moyenne >= 14:
    mention = "Bien"
elif moyenne >= 12:
    mention = "Assez bien"
elif moyenne >= 10:
    mention = "Passable"
else:
    mention = "Ajourné"

# Affichage du bulletin complet
print("\n===============================")
print("        BULLETIN SCOLAIRE      ")
print("===============================\n")
print("Nom :", nom)
print("Prénom :", prenom)
print("\nNotes :")
print(f"- Français       : {note1} / 20")
print(f"- Anglais        : {note2} / 20")
print(f"- Physique       : {note3} / 20")
print(f"- Mathématiques  : {note4} / 20")
print(f"- Sport          : {note5} / 20")
print(f"\nMoyenne générale : {moyenne} / 20")
print("Mention :", mention)
