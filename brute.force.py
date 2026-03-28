liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]


mot = input('Entrez votre mot de passe : ')
chaine = str()
run=True

while run==True:
        def test(chaine,mot):
            if chaine == mot:
                print(mot)
                print('Le mot de passe est :')
                print(mot)
                sys.exit()
            
        for l in liste:
            chaine = l
            test(chaine,mot)
                                                     
            for l2 in liste:
                chaine = l + l2
                test(chaine,mot)
                print(chaine)

                for l3 in liste:
                    chaine = l + l2 + l3
                    test(chaine,mot)
                    print(chaine)

                    for l4 in liste:
                        chaine = l + l2 + l3 + l4
                        test(chaine, mot)
                        print(chaine)

                        for l5 in liste:
                            chaine = l + l2 + l3 + l4 + l5
                            test(chaine, mot)
                            print(chaine)


