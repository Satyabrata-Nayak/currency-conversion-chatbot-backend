from flask import Flask,request,jsonify
import requests
app = Flask(__name__)


def conversion_factor(source,target):
    try:
        url='https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{}.json'.format(source.lower())
        data = requests.get(url).json()
        cf = data[source.lower()][target.lower()]
        return cf
    except:
        url='https://latest.currency-api.pages.dev/v1/currencies/{}.json'.format(source.lower())
        data = requests.get(url).json()
        cf = data[source.lower()][target.lower()]
        return cf


@app.route('/',methods=["GET",'POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    destination_currency = data['queryResult']['parameters']['currency-name']
    final_amount =  round(amount * conversion_factor(source_currency,destination_currency),2)
    response = {
        'fulfillmentText':'{} {} is {} {}'.format(amount,source_currency,final_amount,destination_currency)
    }
    return jsonify(response)
if __name__== '__main__':
    app.run(debug=True)