# -*- coding: utf-8 -*- 

import random
import math
import copy


#### REPRESENTATION DES DONNEES
###initialisation des grilles et autres variables de jeu
grid = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]


grid_start = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

]

grid_mid = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", "O", " ", " ", " "],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "O", " ", "X", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]


grid_end = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "X", " ", " ", " ", " ", " ", " ", " ", " "],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "O", "X", " ", " ", " ", " ", " ", " ", " "]

]

grid_x = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "X", " ", " ", " ", " ", " ", " ", " ", " "],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "X", " ", " ", " ", " ", " ", " ", " "]

]

grid_o = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "O", " ", " ", " ", " ", " ", " ", " ", " "]

]


#fonction pour afficher une grille
def afficher_grille(grille):
    a=65 # initialise l'affichage de la lettre A
    for j in range(len(grille)):
        if j < len(grille)-1:
            print(str(j+1), end=" ") # le numéro de chaque ligne
        else :
            print(str(j+1)) # donne la dernière valeur pour que l'affichage commence avec un retrour a la ligne
    for ligne in grille:
        if a == 65 :
            print("-" * (len(ligne) * 2 - 1)) # Afficher la première ligne horizontal pour séparé les chiffre du plateau
        print("|".join(ligne), end=" ") # Afficher chaque ligne avec les éléments ainsi que séparés par "|"
        print(chr(a))  #  montre la lettre associer a la ligne
        print("-" * (len(ligne) * 2 - 1)) # Afficher des lignes horizontales entre les lignes
        a+=1
        


#### SAISIE
###fonctions de verification
#jeux de tests
def est_au_bon_format(coordonnees):
    if coordonnees[0].isalpha() and coordonnees[1:].isdecimal(): #vérifie que la première coordonner est une lettre et le reste un chiffre
        if 2 <= len(coordonnees) <= 3 and 'A' <= coordonnees[0] <= 'Z':  # Vérifie si la ligne est une seule lettre majuscule comprise dans l'aphabet
            return True
    return False 

#verification du format
def test_est_au_bon_format():
    # Test avec des valeurs valides
    assert est_au_bon_format("A1") == True
    assert est_au_bon_format("Z93") == True

    # Test avec des valeurs invalides
    assert est_au_bon_format("a1") == False  # Ligne en minuscule
    assert est_au_bon_format("11") == False  # Ligne est un chiffre
    assert est_au_bon_format("AB") == False  # Colonne est un caractère
    assert est_au_bon_format("AB3") == False  # Ligne avec plus d'un caractère

    assert est_au_bon_format("A1"), "erreur cas classique"
    assert est_au_bon_format("Z0"), "erreur cas classique, lettre sup"
    assert not est_au_bon_format("12"), "erreur lettre en 0 attendu"
    assert not est_au_bon_format("BB"), "erreur chiffre en 1 attendu"
    assert not est_au_bon_format("&("), "erreur symbole"
    print("les tests de format sont Ok !")


def est_dans_grille(coordonnees, grille):
    if est_au_bon_format(coordonnees):
        if 65 <= ord(coordonnees[0])  <= 65 + len(grille) - 1:  # Vérifie si la ligne possède cette lettre
            if 1 <= int(coordonnees[1:]) <= len(grille):  # regarde si la colonne est est comprise dans la taille des colonne
                return True 
    return False

#verification dans grille
def test_est_dans_grille(grille):
    # Test avec des valeurs valides
    assert est_dans_grille("A1", grille) == True
    assert est_dans_grille("J10", grille) == True    
    
    # Test avec des coordonnées invalides
    assert est_dans_grille("A0", grille) == False  # Colonne inférieure à 1
    assert est_dans_grille("K5", grille) == False  # Ligne supérieure à la taille de la grille
    assert est_dans_grille("E15", grille) == False  # Colonne supérieure à la taille de la grille
    
    assert est_dans_grille("A5",grille),"erreur cas dans la grille"

    grille_bis = [[0]*8]*8

    assert est_dans_grille("A8",grille_bis) == True, "coordonner correct"

    assert not est_dans_grille("a5",grille_bis),"erreur hors ligne inferieure"
    assert not est_dans_grille("I5",grille_bis),"erreur hors ligne superieure"
    assert not est_dans_grille("A-1",grille_bis),"erreur hors colonne inferieure"
    
    print("Les tests de grille sont Ok !")

#vérifie les pions
def est_pion_de(joueur, coordonnees, grille):
    if joueur == grille[ord(coordonnees[0]) - 65][int(coordonnees[1:]) - 1]: #regarde si la case est celle demander par le joueur (vide ou son pion)
        return True
    return False

def test_est_pion_de():
    # Test avec un pion appartenant au joueur X
    assert est_pion_de("X", "I4", grid_start) == True

    # Test avec un pion appartenant au joueur O
    assert est_pion_de("O", "G2", grid_start) == True

    # Test avec une case vide
    assert est_pion_de("X", "E5", grid_start) == False

    # Test avec un pion n'appartenant pas au joueur
    assert est_pion_de("X", "G2", grid_start) == False

    print("Les tests de est_pion_de sont Ok !")

#vérifier le déplacement suivent les règle
def verification_deplacement(coordonnees_1, coordonnees_2):
    #sépare les coordonner
    ligne_1, colonne_1 = ord(coordonnees_1[0]), int(coordonnees_1[1:])
    ligne_2, colonne_2 = ord(coordonnees_2[0]), int(coordonnees_2[1:])

    #vérifie que le pion soit bien déplacé sur une case à devant, arrière, gauche, ou droite de lui.
    if abs(ligne_2 - ligne_1) > 1 or abs(colonne_2 - colonne_1) > 1:
        return False

    if abs(ligne_2 - ligne_1) == 1 and abs(colonne_2 - colonne_1) == 1:
        return False

    return True

def test_verification_deplacement():
    # Tests avec des déplacements autorisés
    assert verification_deplacement("A1", "A2") == True
    assert verification_deplacement("A1", "B1") == True

    # Tests avec des déplacements non autorisés
    assert verification_deplacement("A1", "C1") == False  # Déplacement de 2 cases en ligne droite
    assert verification_deplacement("A1", "B2") == False  # Diagonale
    assert verification_deplacement("A1", "B3") == False  # Déplacement diagonal

    print("Les tests de verification de deplacement sont Ok !")



#vérifie de jeu (fin/mode/start)
def fin(grille):
    x = 0
    o = 0
    for i in range(len(grille)): #regarde chaque ligne
        for j in range(len(grille[i])): #regarde chaque colonne
            if grille[i][j] == "O": 
                o+=1 #compte les "O"
            if grille[i][j] == "X": 
                x+=1 #compte les "X"

    #si l'un des 2 joueur n'a plus de pion alors la fin devient True
    if o == 0 :
        return True
    if x == 0 :
        return True
    return False

def test_fin():
    # Test avec une grille en cours de jeu
    assert fin(grid) == False

    # Test avec une grille WIN pour X
    assert fin(grid_x) == True

    # Test avec une grille WIN pour O
    assert fin(grid_o) == True

    print("Les tests de fin sont Ok !")


def choisir_mode_jeu(): #permet de choisir son mode de jeu
    while True:
        mode = input("Choisissez le mode de jeu (JCJ pour Joueur contre Joueur, JCO pour Joueur contre Ordinateur, TEST qui effectue les test, IA qui permet de jouer contre l'ia avancer) : ").upper()
        if mode == "JCJ" or mode == "JCO" or mode == "TEST" or mode == "IA":
            return mode
        print("Veuillez choisir entre JCJ et JCO et TEST et IA.")

def j_start(): #permet de lancer le jeu en choisissant son pion
    while True:
        choix = input("Le joueur qui commence est (O ou X) : ").upper()
        if choix == "O" or choix == "X":
            return choix
        print("Vous devez choisir entre O et X.")


###fonctions de saisie
def saisir_coordonnees(grille):
    while True:
        coordonnees = input("Entrez les coordonnées (exemple : A1) : ").upper() #saisie les coordonner
        if est_dans_grille(coordonnees, grille):
            return coordonnees
        else:
            print("Coordonnées invalides. Veuillez réessayer.")

###fonction de logique (utilise : saisie/vérification)
def choisir_pion_a_deplacer(grille, joueur): # permet de choisir qu'elle pion sera déplacer
    print("Choisissez le pion à déplacer.")
    while True:
        coordonnees_1 = saisir_coordonnees(grille)
        if est_pion_de(joueur, coordonnees_1, grille):
            return coordonnees_1
        print("Le pion n'est pas à vous ou alors la case est vide.")

def deplacer_pion(grille, joueur, coordonnees_1): # déplace le pion
    print("Choisissez où le déplacer.")
    while True:
        coordonnees_2 = saisir_coordonnees(grille)
        if est_pion_de(" ", coordonnees_2, grille) and verification_deplacement(coordonnees_1, coordonnees_2):
            grille[ord(coordonnees_1[0]) - 65][int(coordonnees_1[1:]) - 1] = " "
            grille[ord(coordonnees_2[0]) - 65][int(coordonnees_2[1:]) - 1] = joueur
            if capture(grille, joueur, coordonnees_2):
                print(f"Le joueur {joueur} a capturé un pion adverse!")
            afficher_grille(grille)
            return True
        print("La case est occupée ou les coordonnées ne sont pas valides/autorisées.")

def deplacement(grille, joueur): # sert a utiliser les outils pour déplacer un pion
    coordonnees_1 = choisir_pion_a_deplacer(grille, joueur)
    return deplacer_pion(grille, joueur, coordonnees_1)



def capture(grille, joueur, coordonnees): # sert a utiliser les outils de capture et donc à capturer

    ligne, colonne = ord(coordonnees[0]) - 65, int(coordonnees[1:]) - 1
    
    if capture_horizontale(grille, joueur, ligne, colonne):
        return True
    if capture_verticale(grille, joueur, ligne, colonne):
        return True
    
    return False

def capture_horizontale(grille, joueur, ligne, colonne): # Vérifie si un pion adverse peut être capturé horizontalement.
   
    adversaire = "O" if joueur == "X" else "X"
    
    # Vérifier à gauche
    if colonne > 0 and grille[ligne][colonne - 1] == adversaire:
        if colonne == 1 or grille[ligne][colonne - 2] == joueur:
            grille[ligne][colonne - 1] = " "
            return True
    
    # Vérifier à droite
    if colonne < 9 and grille[ligne][colonne + 1] == adversaire:
        if colonne == 8 or grille[ligne][colonne + 2] == joueur:
            grille[ligne][colonne + 1] = " "
            return True
    
    return False

def capture_verticale(grille, joueur, ligne, colonne): #  Vérifie si un pion adverse peut être capturé verticalement.

    adversaire = "O" if joueur == "X" else "X"
    
    # Vérifier en haut
    if ligne > 0 and grille[ligne - 1][colonne] == adversaire:
        if ligne == 1 or grille[ligne - 2][colonne] == joueur:
            grille[ligne - 1][colonne] = " "
            return True
    
    # Vérifier en bas
    if ligne < 9 and grille[ligne + 1][colonne] == adversaire:
        if ligne == 8 or grille[ligne + 2][colonne] == joueur:
            grille[ligne + 1][colonne] = " "
            return True
    
    return False

# fonction ia naive

def selectionner_pion_valide(grille, joueur): # sélection un pion valide pour l'ia naive
    pions_valides = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == joueur:
                pions_valides.append((i, j))
    return random.choice(pions_valides) if pions_valides else None

def test_selectionner_pion_valide():
    grille = [
        [" ", " ", " ", " ", " "],
        [" ", "O", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", "X", " "],
        [" ", " ", " ", " ", " "]
    ]
    joueur = "O"
    pion = selectionner_pion_valide(grille, joueur)
    assert pion == (1, 1)  # Attendu : Coordonnées d'un pion "O" valide
    print ("test_selectionner_pion_valide ok !")

def choisir_direction(grille, pion): #choisi un direction pour l'ia naive
    directions_possibles = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Droite, Gauche, Bas, Haut

    for direction in directions:
        destination = calculer_destination(pion, direction)
        if 0 <= destination[0] < len(grille) and 0 <= destination[1] < len(grille[0]) and grille[destination[0]][destination[1]] == " ":
            directions_possibles.append(direction)

    return random.choice(directions_possibles) if directions_possibles else None

def test_choisir_direction():
    grille = [
        [" ", " ", " ", " ", " "],
        [" ", "O", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", "X", " "],
        [" ", " ", " ", " ", " "]
    ]
    pion = (1, 1)
    direction = choisir_direction(grille, pion)
    assert direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Attendu : Une direction valide pour le déplacement
    print ("test_choisir_direction ok !")

def calculer_destination(pion, direction): # calcul la destination de l'ia naive
    return pion[0] + direction[0], pion[1] + direction[1]


def test_calculer_destination():
    pion = (1, 1)
    direction = (0, 1)
    destination = calculer_destination(pion, direction)
    assert destination == (1, 2)  # Attendu : La destination calculée à partir du pion et de la direction
    print ("test_calculer_destination ok !")


def choisir_deplacement_aleatoire(grille, joueur): # permet d'utiliser les outils de l'ia naive et de géré les capture de l'ia naive
    pion = selectionner_pion_valide(grille, joueur)
    if not pion:
        return None, None
    
    direction = choisir_direction(grille, pion)  # Fournir grille et pion comme arguments
    destination = calculer_destination(pion, direction)
    
    if 0 <= destination[0] < len(grille) and 0 <= destination[1] < len(grille[0]) and grille[destination[0]][destination[1]] == " ":
        grille[destination[0]][destination[1]] = joueur
        grille[pion[0]][pion[1]] = " "
        if capture(grille, joueur, chr(pion[0] + 65) + str(pion[1] + 1)):  # Convertir les coordonnées en chaîne de caractères
            print(f"Le joueur {joueur} a capturé un pion adverse!")
    afficher_grille(grille)
    return pion, destination

def test_choisir_deplacement_aleatoire():
    grille = [
        [" ", " ", " ", " ", " "],
        [" ", "O", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", "X", " "],
        [" ", " ", " ", " ", " "]
    ]
    joueur = "O"
    pion, destination = choisir_deplacement_aleatoire(grille, joueur)
    assert pion == (1, 1)  # Attendu : Coordonnées du pion sélectionné
    assert destination in [(0, 1), (1, 0), (2, 1), (1, 2)]  # Attendu : Destination valide pour le déplacement
    print ("test_choisir_deplacement_aleatoire ok !")


### Ia Avancé ###

def evaluer_position(grille, joueur): # Évalue la position actuelle de l'ia sur le plateau a partir de menace et de capture
    score = 0
    
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == joueur:
                # Vérification des possibilités de captures
                score += evaluer_possibilite_capture(grille, i, j, joueur)
            elif grille[i][j] == adversaire(joueur):
                # Vérification des menaces adverses
                score -= evaluer_menace(grille, i, j, adversaire(joueur))

    return score

def evaluer_possibilite_capture(grille, i, j, joueur): #  Évalue le nombre de captures possibles pour un pion de l'ia
    score = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for di, dj in directions:
        # Initialisation des variables pour la recherche de captures dans une direction
        k = 1
        captures_possibles = 0
        adversaire_trouve = False
        while True:
            new_i = i + k * di
            new_j = j + k * dj
            # Vérifier si les nouvelles coordonnées sont à l'intérieur du plateau
            if 0 <= new_i < len(grille) and 0 <= new_j < len(grille[0]):
                if grille[new_i][new_j] == adversaire(joueur):
                    adversaire_trouve = True
                    k += 1
                elif grille[new_i][new_j] == joueur and adversaire_trouve:
                    captures_possibles += k - 1
                    break
                else:
                    break
            else:
                break
        # Ajouter le nombre de captures possibles dans cette direction au score total
        score += captures_possibles

    return score

def evaluer_menace(grille, i, j, adversaire): # Évalue le nombre de menaces potentielles qu'un pion adverse pourrait représenter pour l'ia
    menace_score = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for di, dj in directions:
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < len(grille) and 0 <= new_j < len(grille[0]) and grille[new_i][new_j] == adversaire:
            menace_score += 1

    return menace_score

# Algorithme Minimax avec élagage alpha-bêta
def minimax(grille, profondeur, joueur_max, joueur_actuel, alpha, beta): # détermine le meilleur coup en évaluant les différentes positions possibles.
    if profondeur == 0 or fin(grille):
        return evaluer_position(grille, joueur_actuel), None

    if joueur_max:
        return maximiser(grille, profondeur, joueur_actuel, alpha, beta)
    else:
        return minimiser(grille, profondeur, joueur_actuel, alpha, beta)

def maximiser(grille, profondeur, joueur_actuel, alpha, beta): # maximise le score de l'ia en explorant les coups possibles.
    meilleur_score = -math.inf
    meilleur_coup = None
    for coup in coups_possibles(grille, joueur_actuel):
        nouvelle_grille = jouer_coup(grille, coup, joueur_actuel)
        score, _ = minimax(nouvelle_grille, profondeur - 1, False, joueur_actuel, alpha, beta)
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = coup
        alpha = max(alpha, score)
        if beta <= alpha:
            break
    return meilleur_score, meilleur_coup

def minimiser(grille, profondeur, joueur_actuel, alpha, beta): # minimise le score de l'ia en explorant les coups possibles de l'adversaire.
    pire_score = math.inf
    pire_coup = None
    for coup in coups_possibles(grille, adversaire(joueur_actuel)):
        nouvelle_grille = jouer_coup(grille, coup, adversaire(joueur_actuel))
        score, _ = minimax(nouvelle_grille, profondeur - 1, True, joueur_actuel, alpha, beta)
        if score < pire_score:
            pire_score = score
            pire_coup = coup
        beta = min(beta, score)
        if beta <= alpha:
            break
    return pire_score, pire_coup


def coups_possibles(grille, joueur): # Obtenir tous les coups possibles
    coups = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == joueur:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_i = i + di
                    new_j = j + dj
                    if 0 <= new_i < len(grille) and 0 <= new_j < len(grille[0]) and grille[new_i][new_j] == " ":
                        coups.append((i, j, new_i, new_j))
    return coups


def jouer_coup(grille, coup, joueur): # permet a l'ia avancer de jouer sont coup
    nouvelle_grille = copy.deepcopy(grille)
    i, j, new_i, new_j = coup
    nouvelle_grille[new_i][new_j] = joueur
    nouvelle_grille[i][j] = " "

    # Vérifier les captures après le déplacement
    capture(nouvelle_grille, joueur, chr(new_i + 65) + str(new_j + 1))
    return nouvelle_grille

# Obtenir le joueur adversaire
def adversaire(joueur):
    return "O" if joueur == "X" else "X"

# Fonction principale pour jouer contre l'IA
def jouer_contre_ia(): #permet le système de tour par tour avec l'ia avancer
    grille = grid
    afficher_grille(grille)
    joueur = j_start()
    ia = adversaire(joueur)

    while not fin(grille):
        if joueur == ia:
            _, coup = minimax(grille, 3, True, ia, -math.inf, math.inf)
            grille = jouer_coup(grille, coup, ia)
            print(f"L'IA a joué : {coup}")
        else:
            deplacement(grille, joueur)
        afficher_grille(grille)
        joueur = adversaire(joueur)

    print("Le jeu est terminé !")


### appelle Test ###

# # # #execution test est_au_bon_format
# test_est_au_bon_format() # permet de verifier le vérificateur de saisie

# # # #execution test est_dans_grille
# test_est_dans_grille(grid_start) # uniquement pour la mise au point, a conserver pour le correcteur

# # # #affichage des coordonnees/déplacement/pion/fin
# #print(saisir_coordonnees(grid_start))
# #deplacement(grid,"O")
# test_verification_deplacement()
# test_est_pion_de()       
# test_fin()

# # test ia naïve
# test_selectionner_pion_valide()
# test_choisir_direction()
# test_calculer_destination()
# test_choisir_deplacement_aleatoire()

# test ia naïve a plusiseurs test car aléatoire
# for i in range(100):
#     test_selectionner_pion_valide()
#     test_choisir_direction()
#     test_calculer_destination()
#     test_choisir_deplacement_aleatoire()
# print ("prog aléatoire ok !!!")

#### CODE PRINCIPAL
#execution affichage sur les 3 grilles et autres variables de jeux
start = 0
grille = grid
mode_jeu = choisir_mode_jeu()
if mode_jeu == "TEST":
    # # #execution test est_au_bon_format
    test_est_au_bon_format() # permet de verifier le vérificateur de saisie

    # # #execution test est_dans_grille
    test_est_dans_grille(grid_start) # uniquement pour la mise au point, a conserver pour le correcteur

    # # #affichage des coordonnees/déplacement/pion/fin
    #print(saisir_coordonnees(grid_start))
    #deplacement(grid,"O")
    test_verification_deplacement()
    test_est_pion_de()       
    test_fin()

    # test ia naïve
    test_selectionner_pion_valide()
    test_choisir_direction()
    test_calculer_destination()
    test_choisir_deplacement_aleatoire()

if mode_jeu == "JCO":
    start = 1
    joueur = input("Choisissez votre pion (O ou X) : ").upper()
    if joueur == "O":
        ordinateur = "X"
    else:
        ordinateur = "O"
    # Initialisez joueur_suivant en fonction de joueur
    joueur_suivant = "X" if joueur == "O" else "O"
elif mode_jeu == "JCJ":
    start = 1
    joueur = j_start()
    ordinateur = None
    if joueur == "O":
        joueur_suivant = "X"
    else:
        joueur_suivant = "O"
elif mode_jeu == "IA" :
    jouer_contre_ia()

if start == 1 :
    afficher_grille(grille)

    while not fin(grille):
        if ordinateur == joueur:
            pion, destination = choisir_deplacement_aleatoire(grille, ordinateur)
            if pion and destination:  # Vérifie si un déplacement est possible
                grille[destination[0]][destination[1]] = ordinateur
                grille[pion[0]][pion[1]] = " "
                print("L'ordi a joué")
        else:
            deplacement(grille, joueur)
        joueur, joueur_suivant = joueur_suivant, joueur

    print("Le jeu est terminé !")
