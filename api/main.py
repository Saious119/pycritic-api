from flask import Flask, render_template
import urllib
from urllib.parse import unquote
import json
import os
import api.pycritic

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Fuckers"

@app.route('/game/<platform>/<name>')
def get_metacritic(platform, name):
    url = "https://www.metacritic.com/game/"+platform+"/"+name
    scraper = pycritic.Scraper()
    game = scraper.get(url)
    jsonData = json.dumps(game.__dict__)
    return jsonData

@app.route('/game/metaurl/<path:url>')
def get_metacritic_by_url(url):
    decodedUrl = urllib.parse.unquote(url)
    scraper = pycritic.Scraper()
    game = scraper.get(decodedUrl)
    jsonData = json.dumps(game.__dict__)
    return jsonData

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))