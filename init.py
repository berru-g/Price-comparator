"""   Price-comparator
      Learn python 
      github/berru-g 23 
"""
import tkinter as tk
import time
import math
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

product_label = tk.Label(root, text="Price:", foreground="#f1faee")
product_label.grid(row=1, column=0, padx=10, pady=10)
product_label.config(bg="#1d3557")
product_entry = tk.Entry(root)
product_entry.grid(row=0, column=1, padx=10, pady=10)

location_label = tk.Label(root, text="Recherche Produit", foreground="#f1faee")
location_label.grid(row=0, column=0, padx=10, pady=10)
location_label.config(bg="#1d3557")
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=1, padx=10, pady=10)

results_text = tk.Text(root)
font_style = ("Helvetica", 12)
#results_text = tk.Text(font=font_style, height=10, width=50)
results_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def search():
    product = product_entry.get()
    location = location_entry.get()
    
    #https://www.amazon.fr/s?k=arduino+component&language=fr_FR&crid=AQBXL9USLKCE&linkCode=sl2&linkId=1ab2135daf6e0bded135d63b11fbba40&sprefix=%2Caps%2C290&tag=makeandplay24-21&ref=as_li_ss_tl# search firstsite.com  # bug de la requete 'location', essaie d'inverser lieux et motcles comme dans lurl dorigine, puis change l'ordre de format, product, location= sans succes
    firstsite_url = "https://www.amazon.fr/s?k={}&language=fr_FR&tag=makeandplay24-21" # 'location' not taken into account. because not "=" in url? 
    firstsite_search = requests.get(firstsite_url.format(product,location))
    firstsite_soup = BeautifulSoup(firstsite_search.text, "html.parser")
    firstsite_titles = firstsite_soup.find_all(class_="a-size-base-plus a-color-base a-text-normal")
    subtitles = firstsite_soup.find_all(class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
    prices = firstsite_soup.find_all(class_="a-price-whole")
    results_text.delete('1.0', tk.END)  # Effacer le contenu de la zone de texte des résultats précédents
    results_text.insert(tk.END, "Résultats de la recherche AMAZON:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557", font=("Arial", 14))

    for title, subtitle, price in zip(firstsite_titles, subtitles, prices):
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{price.text}\n", "price")
        results_text.insert(tk.END, "__________\n")
    # Applique les couleurs
    results_text.tag_config("title", foreground=title_color)
    results_text.tag_config("subtitle", foreground=subtitle_color)
    results_text.tag_config("price", foreground=price_color)
    print("resultat first site")
    time.sleep(1) 
    # Search secondsite.com
    secondsite_url ="https://fr.aliexpress.com/w/wholesale-{}.html?&SearchText={}"               
    secondsite_search = requests.get(secondsite_url.format(product,product))
    secondsite_soup = BeautifulSoup(secondsite_search.text, "html.parser")
    secondsite_titles = secondsite_soup.find_all(class_="manhattan--titleText--WccSjUS")
    secondsite_subtitles = secondsite_soup.find_all(class_="manhattan--trade--2PeJIEB")#md:tw-text-xlOld tw-text-2xlOld tw-leading-[1.625rem]
    secondsite_prices = secondsite_soup.find_all(class_="manhattan--price-sale--1CCSZfK")
    results_text.insert(tk.END, "Résultats de la recherche ALIEXPRESS:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557", font=("Arial", 14))

    for title, subtitle, price in zip(secondsite_titles, secondsite_subtitles, secondsite_prices):
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{price.text}\n", "price")
        results_text.insert(tk.END, "__________\n")
    print("resultat second site")
    time.sleep(1)   
    # Search thirdsite.com
    thirdsite_url ="https://www.ebay.fr/sch/i.html?&_nkw={}&_sacat=0"               
    thirdsite_search = requests.get(thirdsite_url.format(product,location))
    thirdsite_soup = BeautifulSoup(thirdsite_search.text, "html.parser")
    thirdsite_titles = thirdsite_soup.find_all(class_="s-item__title")
    thirdsite_subtitles = thirdsite_soup.find_all(class_="s-item__shipping s-item__logisticsCost")
    thirdsite_prices = thirdsite_soup.find_all(class_="s-item__price")
    results_text.insert(tk.END, "Résultats de la recherche EBAY:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557", font=("Arial", 14))

    for title, subtitle, price in zip(thirdsite_titles, thirdsite_subtitles, thirdsite_prices):
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{price.text}\n", "price")
        results_text.insert(tk.END, "__________\n")
    print("resultat third site")
    time.sleep(1) 
      
print("Fin du scrap")

"""# def compare price 
def get_cheapest_price(soup):
    prices = soup.select('.price')
    if prices:
        # Trie les prix par ordre croissant et renvoie le premier
        return sorted(prices, key=lambda x: float(x.text))[0]
    return None
cheapest_price = get_cheapest_price(firstsite_soup)
if cheapest_price:
    print('Le prix le moins cher est:', cheapest_price.text)
else:
    print('Aucun prix n\'a été trouvé')
"""
search_button = tk.Button(root, text="Rechercher", command=search)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
