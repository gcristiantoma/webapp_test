from flask import Flask, jsonify,render_template
import alpaca_trade_api as tradeapi
import os

app = Flask(__name__)

API_KEY = os.environ.get('ALPACA_API_KEY')
API_SECRET = os.environ.get('ALPACA_SECRET_KEY')
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

@app.route('/')
def index():
    # This route will render an HTML file called 'index.html'
    return render_template('index.html')


# @app.route('/price/<symbol>')
# def get_price(symbol):
#     try:
#         # Use get_latest_trade to fetch the latest trade price
#         price = api.get_latest_trade(symbol)
#         # price = latest_trade.p
#         print(type(price))
#         return jsonify({'symbol': symbol, 'price': price})
#     except Exception as e:
#         # If an error occurs, return the error message and a 500 status code
#         return jsonify({'error': str(e)}), 500

@app.route('/price/<symbol>')
def get_price(symbol):
    try:
        latest_trade = api.get_latest_trade(symbol)
        # Directly access the attributes of the TradeV2 object
        trade_data = {
            'price': latest_trade.price,
            'timestamp': latest_trade.timestamp.isoformat() if latest_trade.timestamp else None,
            'size': latest_trade.size,
            'exchange': latest_trade.exchange,
            'tape': latest_trade.tape
        }
        return jsonify(trade_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # get_price("TSLA")
    app.run(debug=True)
