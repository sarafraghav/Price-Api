from flask import Flask , jsonify
from flask_restful import reqparse
import requests
app = Flask(__name__)

url = 'https://prime.exchangerate-api.com/v5/cb4c95ba361e5d2beaba105d/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()


@app.route('/')
def hello_world():
    result = {}
    parser = reqparse.RequestParser()
    parser.add_argument('currency')
    parser.add_argument('priceusd', store_missing=False)
    parser.add_argument('pricecurrency', store_missing=False)
    args = parser.parse_args()
    if 'pricecurrency' in args:
        price = price_quota(int(args['pricecurrency']), str(args['currency']))
        result['USD'] = price
    if 'priceusd' in args:
        usd = dollar_to_inr(int(args['priceusd']), str(args['currency']))
        result['INR'] = usd
    return jsonify(result)






def price_quota(price_wanted , currency):
    price = price_wanted
    exchange_rate = data.get("conversion_rates").get(currency)
    usd_price = price/exchange_rate
    fiverr_asking_price = usd_price/0.8
    return(fiverr_asking_price)

def dollar_to_inr(usd_price , currency):
    pri = usd_price
    exchange_rate = data.get("conversion_rates").get(currency)
    pri = pri*0.8
    final_price = pri*exchange_rate
    return(final_price)





if __name__ == '__main__':
    app.run()
