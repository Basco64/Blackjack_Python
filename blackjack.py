import random

GAME = True
QUATRIEME_CARTE = True
HIT_CROUPIER = 17
MANCHE = True


def tirer_une_carte():
    global carte_valeur
    carte_valeur = random.randint(1, 13)
    carte_couleur = random.randint(1, 4)
    nom_carte = ""

    if carte_couleur == 1:
        carte_couleur = ' de Coeur'
    elif carte_couleur == 2:
        carte_couleur = ' de Pique'
    elif carte_couleur == 3:
        carte_couleur = ' de Tréfles'
    elif carte_couleur == 4:
        carte_couleur = ' de Carreaux'

    if carte_valeur == 1:
        nom_carte = 'As'
    elif carte_valeur == 11:
        nom_carte = 'Valet'
        carte_valeur = 10
    elif carte_valeur == 12:
        nom_carte = 'Dame'
        carte_valeur = 10
    elif carte_valeur == 13:
        nom_carte = 'Roi'
        carte_valeur = 10
    else:
        nom_carte = str(carte_valeur)

    return nom_carte + carte_couleur


print("BlackJack")
print(" ")
print(
    f"Le croupier arrete de tirer ses cartes dés qu'il atteint {HIT_CROUPIER}.")
print("-" * 10)

while GAME == True:

    valeur_user = 0
    valeur_croupier = 0
    As = ''
    continuerTirer = True

    # Mise en place de la table
    premiereCarte = tirer_une_carte()
    print(f"Vous avez tiré : {premiereCarte}")
    if carte_valeur == 1:
        while not (As == '11' or As == '1'):
            As = input(
                "Vous avez tirer un As. Voulez vous qu'il vaille 1 ou 11 ? ")
            if As == '11':
                valeur_user += 11
            elif As == '1':
                valeur_user += 1
    else:
        valeur_user += carte_valeur
    As = ''

    deuxiemeCarte = tirer_une_carte()
    print(f"Le croupiez a tiré : {deuxiemeCarte}")
    if carte_valeur == 1:
        valeur_croupier += 11
    else:
        valeur_croupier += carte_valeur

    troisiemeCarte = tirer_une_carte()
    print(f"Vous avez tiré : {troisiemeCarte}")
    if carte_valeur == 1:
        while not (As == '11' or As == '1'):
            As = input(
                "Vous avez tirer un As. Voulez vous qu'il vaille 1 ou 11 ? ")
            if As == '11':
                valeur_user += 11
            elif As == '1':
                valeur_user += 1
    else:
        valeur_user += carte_valeur
    As = ''

    quatriemeCarte = tirer_une_carte()
    valeur_croupier += carte_valeur

    print(f"Vous avez {valeur_user} points.")
    print(f"Le croupier à {valeur_croupier} points.")

    if valeur_user == 21:
        print(f"Vous avez : {valeur_user} 🎉 BlackJack ! 🎉")
        MANCHE = False
    if valeur_croupier == 21:
        print(
            f"Le croupier à : {valeur_croupier}. Il ne vous aura laissez aucune chance! 😕")
        MANCHE = False

    # Début de la manche
    while MANCHE == True:
        if continuerTirer:
            choix_user = input('Voulez vous tirer une carte? (y/n) ')
            if(choix_user == 'y'):
                user1 = tirer_une_carte()

                print(f"Vous avez tirer : {user1}")
                if carte_valeur == 1:
                    while not (As == '11' or As == '1'):
                        As = input(
                            "Vous avez tirer un As. Voulez vous qu'il vaille 1 ou 11 ? ")
                        if As == '11':
                            valeur_user += 11
                        elif As == '1':
                            valeur_user += 1
                else:
                    valeur_user += carte_valeur
            else:
                continuerTirer = False
            As = ''

            if valeur_user > 21:
                print(f"Vous avez: {valeur_user} Perdu !")
                break

            if valeur_user == 21 and valeur_croupier >= HIT_CROUPIER:
                print('✨ Bien joué ! Vous avez gagnez. ✨')
                break

            print(f'Vous avez : {valeur_user} points.')
            if QUATRIEME_CARTE:
                print(
                    f"Le croupier retourne sa deuxieme carte : {quatriemeCarte}")
                QUATRIEME_CARTE = False

        if valeur_croupier >= HIT_CROUPIER:
            print("Le croupier n'a plus le droit de piocher.")
            if(choix_user == 'n'):
                print(
                    f"Le croupier a {valeur_croupier} points, vous avez {valeur_user} points.")
                continuerPartie = input(
                    "Souhaitez vous continuer cette manche? (y/n)")
                if continuerPartie == 'n':
                    if(valeur_user == valeur_croupier):
                        print('Egalité.')
                    elif(valeur_user > valeur_croupier):
                        print('✨ Bien joué ! Vous avez gagnez. ✨')
                    else:
                        print('Le croupier a gagner.')
                    break
                if continuerPartie == 'y':
                    continue
        else:
            croupier = tirer_une_carte()
            valeur_croupier += carte_valeur
            print(f"Le croupier à tirer : {croupier}")

            if valeur_croupier > 21:
                print(
                    f"Le croupier à : {valeur_croupier} ✨ Vous avez gagnez ✨")
                break

        print(f'Le croupier est à : {valeur_croupier}')
        print("-" * 30)

    game = input("Voulez vous rejouez une manche? (y/n) ")

    if game == 'y':
        continue
    else:
        break
