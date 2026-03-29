print("Bienvenue tu entres dans un chateau")
run=True
import random

while run == True:
    print("tu à le choix entre 3 portes")
    choixjoueur=input("1,2,3 ou Stopgame")
    a=random.choice(['1', '2', '3'])
    
    if choixjoueur==a:
        print("Bravo tu as gagné")

    elif choixjoueur=="Stopgame":
        run=False

    elif choixjoueur!=a:
        print("Oups tu as perdu")
       
        

    

   
      

        
  
        
          
    

