import requests

# json_data=requests.get('http://www.floatrates.com/daily/idr.json')
json_data= {
    "usd": {
        "code": "USD",
        "alphaCode": "USD",
        "numericCode": "840",
        "name": "U.S. Dollar",
        "rate": 6.8802180015921e-5,
        "date": "Mon, 6 Jul 2020 12:00:01 GMT",
        "inverseRate": 14534.423179158
    },
    "eur": {
        "code": "EUR",
        "alphaCode": "EUR",
        "numericCode": "978",
        "name": "Euro",
        "rate": 6.1059459835592e-5,
        "date": "Mon, 6 Jul 2020 12:00:01 GMT",
        "inverseRate": 16377.478652654
    }}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
