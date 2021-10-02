
print('\nWelcome to our quiz!')
print('You have 3 lives.')
print('-------')

count = 3

liste=["\n**Question 1 : Combien font 1+1 ? ",
       "\n**Question 2 : Quel est le nom du président français ? ",
       "\n**Question 3 : Quel est le premier jour de la semaine ? ",
       "2", "macron", "lundi"]

ma_valeur = input(liste[0]).lower()
ma_valeur = str(ma_valeur)
print("Votre réponse est :", ma_valeur)

for i in liste[3]:
    if ma_valeur == liste[3] and count != 0:
        print("Bien joué", ma_valeur, "est la bonne réponse")
    if ma_valeur != liste[3] and count != 0:
        count -= 1
        print("Sorry you have", count, "chances left")
        if count == 0:
            print("Vous avez perdu")
    else:
        ma_valeur = input(liste[0]).lower()
        ma_valeur = str(ma_valeur)

ma_valeur=input(liste[1]).lower()
ma_valeur=str(ma_valeur)

for i in liste[4]:
    if ma_valeur == liste[4] and count != 0:
        print("bien joué")
        break
    if ma_valeur != liste[4] and count !=0:
        print("faux")
        count -=1
        print("Il vous reste", count, "vies")
    if count == 0:
        print("Vous avez perdu")
        break
    ma_valeur = input(liste[1]).lower()
    ma_valeur = str(ma_valeur)


ma_valeur=input(liste[2]).lower()
ma_valeur=str(ma_valeur)

for i in liste[5]:
    if ma_valeur == liste[5] and count != 0:
        print("bien joué")
        break
    if ma_valeur != liste[5] and count !=0:
        print("faux")
        count -=1
        print("Il vous reste", count, "vies")
    if count == 0:
        print("Vous avez perdu")
        break
    ma_valeur = input(liste[2]).lower()
    ma_valeur = str(ma_valeur)

if count != 0:
    print("Vous avez gagné")

