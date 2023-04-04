import webbrowser
import time
product = input('Quel produit cherche tu? ')
url = "https://www.amazon.fr/s?k="
lienAff = "&tag=price-comberu-21"

print("Produit trouver sur Amazon")
print("Voulez-vous ouvrir la page web ? oui / non")
reponse_web = input()
if reponse_web.lower() == "oui":
    webbrowser.open(url+product+lienAff)
elif reponse_web.lower() == "non":
    print("Vous avez choisi de ne pas ouvrir de page web.")
else:
    print("Je ne comprends pas votre réponse.")
    print("Aide moi à améliorer cet outil, rdv sur github.com/berru-g")
    
time.sleep(1)