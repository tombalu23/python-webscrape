import requests
import bs4


#get page html
my_url='https://www.newegg.com/global/in-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=204377'
page = requests.get(my_url)

page_soup= bs4.BeautifulSoup(page.text, 'html.parser')
#print(page_soup)

containers=page_soup.find_all('div', {'class':'item-container'})
print(containers[0])


