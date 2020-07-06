import requests
import bs4
from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('base.html')
@app.route('/detik-populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler'
    html_doc = requests.get(url, params={'tag_from': 'wp_cb_mostPopular_more'})
    soup = bs4.BeautifulSoup(html_doc.text, 'html.parser')
    popular_area = soup.find(attrs={'class': 'grid-row list-content'})
    titles = popular_area.find_all(attrs={'class': 'media__title'})
    images = popular_area.find_all(attrs={'class': 'media__image'})
    print(images)
    return render_template('detik-scraper.html', images=images)

@app.route('/idr-rates')
def idr_rates():
    json_data = requests.get('http://www.floatrates.com/daily/idr.json').json()
    return render_template('idr-rates.html', datas=json_data)

if(__name__=='__main__'):
    app.run(debug=True)