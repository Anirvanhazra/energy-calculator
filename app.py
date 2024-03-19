from flask import Flask

from calculator import get_baltic_electricity_prices

app = Flask(__name__)

@app.route('/')
def get_prices():
    prices = get_baltic_electricity_prices()
    return prices

if __name__ == '__main__':
    app.run()