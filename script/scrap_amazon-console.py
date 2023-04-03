"""    Learn python 
      github/berru-g 23
"""
#next step: interface web
import time
import requests
from bs4 import BeautifulSoup

# Get user input for product 
print("Entrez le produit recherché:")
product = input("")

# URL templates for each site + &tag=makeandplay24-21
first_url = "https://www.amazon.fr/s?k={}"

# Search first
first_search = requests.get(first_url.format(product))
first_soup = BeautifulSoup(first_search.text, "html.parser")
first_titles = first_soup.find_all(class_="a-size-base-plus a-color-base a-text-normal")
subtitles = first_soup.find_all(class_="a-size-base")
dates = first_soup.find_all(class_="a-price-whole")

print("Résultats de la recherche sur Amazon:")

# Print the titles
for title in first_titles:
    for subtitle in subtitles:
        for date in dates:
            print(title.text)
            print(subtitle.text)
            print(date.text)
            print("__________")

print("Fin des résultats")
print("Retrouvez les bon plans Amazon du moment")
print("https://amzn.to/3m3Ol7n")
time.sleep(4)
exit()
