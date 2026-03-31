liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
# Liste de tous les caractères possibles

mot = input('Entrez votre mot de passe : ')  # L'utilisateur tape un mot de passe
chaine = str()  # Variable vide pour tester des combinaisons
run=True  # Variable pour faire tourner la boucle

# Boucle infinie
while run==True:
    
        # Fonction qui teste si on a trouvé le bon mot
        def test(chaine,mot):
            if chaine == mot:  # Si la combinaison = mot de passe
                print(mot)
                print('Le mot de passe est :')
                print(mot)
                sys.exit()  
            
        # On commence avec 1 caractère
        for l in liste:
            chaine = l
            test(chaine,mot)
                                                     
            # Puis 2 caractères
            for l2 in liste:
                chaine = l + l2
                test(chaine,mot)
                print(chaine)  # On affiche chaque test

                # Puis 3 caractères
                for l3 in liste:
                    chaine = l + l2 + l3
                    test(chaine,mot)
                    print(chaine)

                    # Puis 4 caractères
                    for l4 in liste:
                        chaine = l + l2 + l3 + l4
                        test(chaine, mot)
                        print(chaine)

                        # Puis 5 caractères
                        for l5 in liste:
                            chaine = l + l2 + l3 + l4 + l5
                            test(chaine, mot)
                            print(chaine)
