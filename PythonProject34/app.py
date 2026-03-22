from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    breweries = []

    if request.method == "POST":
        city = request.form.get("city")

        url = f"https://api.openbrewerydb.org/v1/breweries?by_city={city}"
        response = requests.get(url)

        if response.status_code == 200:
            breweries = response.json()

    return render_template("index.html", breweries=breweries)

if __name__ == "__main__":
    app.run(debug=True)