import requests
import bs4


#get page html
my_url='https://www.newegg.com/global/in-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=204377'
page = requests.get(my_url)

page_soup= bs4.BeautifulSoup(page.text, 'html.parser')
#print(page_soup)


#grabs each product
containers=page_soup.find_all('div', {'class':'item-container'})
#print(containers[0])

filename="graphics_cards.csv"
f = open(filename, 'w')
headers = "BRAND, PRODUCT_NAME, PRICE"
f.write(headers+'\n')



for container in containers:
    itembrand = container.find('div', {'class':'item-branding'})
    brand = itembrand.a.img["title"]
    name=container.a.img['title']
    info=container.find('div', {'class':'item-info'})

    #    price=info.find('div', {'class':'item-action'}).ul.li.text.strip('\r')
    price = info.find('div', {'class': 'item-action'}).ul.find('li', {'class':'price-current'}).text.strip()
    price_float=(price[11:17])
    print(brand + '     ' + name + '    ' + price[:])

    f.write(brand + ',' + name.replace(',', '|') + ',' + price[:].replace('\u20b9',"").replace(',',"").replace('–',"").replace('\n',"").strip() + '\n')

f.close()