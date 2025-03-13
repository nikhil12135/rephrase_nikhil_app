

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "UC6BXQ6WVF60LJ8X95FY5NKQK70YNMNW"

API_URL = "https://api.sapling.ai/api/v1/paraphrase"

@app.route("/", methods=["GET", "POST"])
def index():
    replacements = []  # Use a list to store multiple replacements

    if request.method == "POST":
        text = request.form["text"]  # Get user input
        data = {"key": API_KEY, "text": text}

        try:
            response = requests.post(API_URL, json=data)
            resp_json = response.json()

            print("DEBUG: Full API Response:", resp_json)  # Debugging print

            # Extract replacements from "results"
            if response.status_code == 200 and "results" in resp_json:
                replacements = [result["replacement"] for result in resp_json["results"]]
            else:
                replacements = ["Error: Invalid API response"]

        except Exception as e:
            replacements = ["Error: " + str(e)]

    return render_template("index.html", replacements=replacements)

if __name__ == "__main__":
    app.run(debug=True)
