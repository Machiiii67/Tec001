#1
import requests
def random_joke():
    url = "https://api.chucknorris.io/jokes/random"

    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        return data["value"]
    except requests.RequestException:
        return "Không thể lấy joke từ API."


print(random_joke())
#2
import urllib.request
import urllib.parse
import urllib.error
import json

city = input("Enter municipality name: ").strip()
api_key = "8a925c820f3fbbbf34116dd2d2c83fb9"

url = "https://api.openweathermap.org/data/2.5/weather?" + urllib.parse.urlencode({
    "q": city,
    "appid": api_key,
    "units": "metric"
})

print(url)

try:
    res = urllib.request.urlopen(url)
    raw_data = res.read().decode()
    print(raw_data)

    data = json.loads(raw_data)
    print("Weather condition:", data["weather"][0]["description"])
    print("Temperature:", data["main"]["temp"], "°C")

except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code)
    print(e.read().decode())
except urllib.error.URLError as e:
    print("URL Error:", e.reason)
except Exception as e:
    print("Other Error:", e)
#3
from flask import Flask, jsonify
app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })

if __name__ == '__main__':
    app.run(debug=True)
#4
from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("airports.json", "r", encoding="utf-8") as file:
    airports = json.load(file)

@app.route("/airport/<icao>", methods=["GET"])
def get_airport(icao):
    icao = icao.upper()

    for airport in airports:
        if airport["icao"] == icao:
            return jsonify({
                "icao": airport["icao"],
                "name": airport["name"],
                "city": airport["municipality"],
                "country": airport["iso_country"]
            })

    return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)