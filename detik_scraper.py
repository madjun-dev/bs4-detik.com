import bs4
import requests

url='https://www.detik.com/terpopuler'
html_doc=requests.get(url, params={'tag_from':'wp_cb_mostPopular_more'})
soup= bs4.BeautifulSoup(html_doc.text,'html.parser')
popular_area=soup.find(attrs={'class':'grid-row list-content'})
titles=popular_area.find_all(attrs={'class':'media__title'})
images=popular_area.find_all(attrs={'class':'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])
# for title in titles:
#     print(title.text)