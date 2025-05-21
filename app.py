from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

BASE_URL = "https://www.moldinsolv.md"
SEARCH_URL = BASE_URL + "/?s={query}"

def cauta_pe_moldinsolv(cuvant_cheie):
    url = SEARCH_URL.format(query=cuvant_cheie)
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return []

    soup = BeautifulSoup(r.text, 'html.parser')
    rezultate = []
    for a in soup.select('.entry-title a'):
        titlu = a.get_text(strip=True)
        href = a.get('href')
        rezultate.append({"titlu": titlu, "url": href})
    return rezultate[:5]

@app.route("/cauta", methods=["GET"])
def cauta():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Furnizează un cuvânt cheie în parametrul ?q="}), 400

    rezultate = cauta_pe_moldinsolv(query)
    if not rezultate:
        return jsonify({"mesaj": "Nu am găsit informații relevante pe moldinsolv.md."})

    return jsonify({"rezultate": rezultate})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
