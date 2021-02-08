from flask import render_template, Flask
import requests

app = Flask(__name__)

# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Random joke from chuck norris: </strong>" + response['value']
