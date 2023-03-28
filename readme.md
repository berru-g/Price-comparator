## Comparateur de prix .py 
### *work in progress*

    pip install tkinter, requests, BeautifulSoup

### Scrapping de produit 

## script\scrapping-ecommerce-interface.py =
## Scrapp

    - Amazon
    - Aliexpress
    - Ebay

<img width="499" alt="Capture d'écran_20230322_091500" src="https://user-images.githubusercontent.com/61543927/226840798-690cbe0c-2c4e-495e-b361-176182685559.png">

<img width="499" alt="Capture d'écran_20230322_091518" src="https://user-images.githubusercontent.com/61543927/226840824-b24281f9-8465-4272-9ddd-d8b14aeae628.png">

<img width="495" alt="Capture d'écran_20230322_091533" src="https://user-images.githubusercontent.com/61543927/226840846-52d4b4d1-e001-415f-92c3-f0032a4190eb.png">

## script\scrapping-low-price-interface.py =
## Scrap Ebay & get_lowest_price *non fonctionnel*

    - Ebay (only w i p...)
    
    
<img width="498" alt="Capture d'écran_20230323_164600" src="https://user-images.githubusercontent.com/61543927/227258639-3d3dbaae-d1ab-41ba-b58a-41ae6272b90a.png">
    
<img width="498" alt="Capture d'écran_20230323_164616" src="https://user-images.githubusercontent.com/61543927/227258697-38ea8043-0aa4-4d0e-a784-5772cc1c4cd8.png">



#### *Passer par un env virtuel comme VM + VPN* Car le scrapp peut être sanctionné!




### Logique 

  

```mermaid

  

sequenceDiagram

  

User ->> App: Search product?

  

S_1-->>S_2: Cherche?

  

S_1--x Compare: Selectionne!

  

Compare-x App: Lien affiliation!

  

Note right of S_2: Compare le prix,<br/>selectionne,<br/>Ajout lien aff,<br/>Envoie lien aff.


  

Compare-->>User: Achat?

  

```

projet en cours:

> Work in progress. [Involve](https://github.com/berru-g/).


