import webbrowser
import time
print('''
           ==========Amazon for family===========
           1. Ecrit ton produit recherché
           2. Choisi oui pour ouvrir le lien Amz
           3. Si tu achète sous 24H j'ai une commission
           4. Cela ne change rien pour toi
           5. Merci du soutien'''
             )
product = input('Quel produit cherche tu? ')
url = "https://www.amazon.fr/s?k="
lienAff = "&tag=price-comberu-21"

print("Produit trouver sur Amazon")
print("Voulez-vous ouvrir la page web ? oui / non")
reponse_web = input()
if reponse_web.lower() == "oui":
    webbrowser.open(url+product+lienAff)
elif reponse_web.lower() == "non":
    print("Vous avez choisi de ne pas ouvrir de page web. Bonne journée")
else:
    print("Je ne comprends pas votre réponse.")
    
    
time.sleep(1)
