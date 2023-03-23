"""Resultat de comparaison cliquable + lien aff"""

def compare():
    products = soup.find_all("div", {"class": "product"})

    lowest_price = float("inf")
    lowest_price_url = "https://www.ebay.fr/sch/i.html?&_nkw={}&_sacat=0"
    lowest_price_title = "s-item__title"
    lowest_price_subtitle = "s-item__shipping s-item__logisticsCost"
    lowest_price_class = "s-item__link"
#s-item__link
    for product in products:
        title = product.find("h2", {"class": "title"}).text.strip()
        subtitle = product.find("p", {"class": "subtitle"}).text.strip()
        price = float(product.find("span", {"class": "price"}).text.strip().replace("$", ""))
        url = product.find("a")["s-item__link"]
        product_class = product.find("a")["class"]
        if price < lowest_price:
            lowest_price = price
            lowest_price_url = url
            lowest_price_title = title
            lowest_price_subtitle = subtitle
            lowest_price_class = product_class

    print(f"Lowest price: ${lowest_price} ({lowest_price_title}, {lowest_price_subtitle})")
    print(f"URL: {lowest_price_url}, Class: {lowest_price_class}")