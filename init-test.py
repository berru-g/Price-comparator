"""   Price-comparator
      Learn python 
      github/berru-g 23 
"""
import tkinter as tk
import time
import math
import re
import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("Comparateur de prix")
#root.iconbitmap('src\logo.png')
#p1 = tk.PhotoImage(file = 'src\logo.png')
#root.iconphoto(False, p1)
root.config(bg="#1d3557") 
title_color = "#1d3557"
subtitle_color = "#2a9d8f"
price_color = "#f4a261"

product_label = tk.Label(root, text="Product:", foreground="#f1faee")
product_label.grid(row=0, column=0, padx=10, pady=10)
product_label.config(bg="#1d3557")
product_entry = tk.Entry(root)
product_entry.grid(row=0, column=1, padx=10, pady=10)

results_text = tk.Text(root)
font_style = ("Helvetica", 12)

results_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


def get_lowest_price(prices):
    # Initialisation de la variable du prix minimum
    min_price = float('inf')
    
    # Boucle pour extraire chaque prix
    for price in prices:
        # Extraire les chiffres du prix en utilisant une expression régulière
        price_digits = re.findall('\d+\.\d+', price.text)
        if price_digits:
            # Convertir les chiffres en float et comparer au prix minimum
            float_price = float(price_digits[0])
            if float_price < min_price:
                min_price = float_price
    
    # Retourner le prix minimum
    return min_price


def search():
    product = product_entry.get()
    #prix = prix_entry.get()
    
    # Scraper le premier site
    firstsite_url = "https://www.ebay.fr/sch/i.html?&_nkw={}&_sacat=0"
    firstsite_search = requests.get(firstsite_url.format(product))
    firstsite_soup = BeautifulSoup(firstsite_search.text, "html.parser")
    firstsite_titles = firstsite_soup.find_all(class_="s-item__title")
    subtitles = firstsite_soup.find_all(class_="s-item__shipping s-item__logisticsCost")
    prices = firstsite_soup.find_all(class_="s-item__price")
    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, "Résultats de la recherche Ebay:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557", font=("Arial", 14))

    # Afficher les résultats pour le premier site
    for title, subtitle, price in zip(firstsite_titles, subtitles, prices):
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{price.text}\n", "price")
        results_text.insert(tk.END, "__________\n")
    firstsite_min_price = get_lowest_price(prices)
    results_text.insert(tk.END, f"Prix minimum sur Ebay: {firstsite_min_price}\n\n", "blue")
    # Applique les couleurs
    results_text.tag_config("title", foreground=title_color)
    results_text.tag_config("subtitle", foreground=subtitle_color)
    results_text.tag_config("price", foreground=price_color)
    print("resultat first site")
    time.sleep(0.5)
     
    
print("Fin du scrap")
print("Compare...")


print("Fin du programme")        
search_button = tk.Button(root, text="Rechercher", command=search)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
