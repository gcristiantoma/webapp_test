from flask import Flask, jsonify
import alpaca_trade_api as tradeapi

app = Flask(__name__)

# Replace with your Alpaca API credentials
API_KEY = 'PKE3ML8XXEH0F1TYLOH4'
API_SECRET = 'ckz6HSEyRsLEho5TefYlcmWjwoF79D3MAtsyWdRA'
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)


def get_price(symbol):
    try:
        # For simplicity, using the last quote endpoint
        last_quote = api.get_latest_trade(symbol)
        # price = last_quote.  # Or .bidprice depending on your need
        print(last_quote)
        return jsonify({'symbol': symbol, 'price': last_quote})
    except Exception as e:
        return {'error': str(e)}

print(get_price("TSLA"))