from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
    try:
        response = requests.get(url).json()
        usd = next(item for item in response if item["ccy"] == "USD")
        eur = next(item for item in response if item["ccy"] == "EUR")
    except Exception as e:
        return f"<h1>Помилка отримання даних: {e}</h1>"

    return f"""
    <h1>Курси валют</h1>
    <p>Гривня / Долар: {usd["buy"]} / {usd["sale"]}</p>
    <p>Гривня / Євро: {eur["buy"]} / {eur["sale"]}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

