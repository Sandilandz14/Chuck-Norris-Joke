from flask import render_template, Flask
import requests

app = Flask(__name__)

# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    my_image = "<image src="+response['icon_url']+" alt='Chuck's Image'>"

    return "<strong>Random joke from Chuck Norris: </strong>" + response['value']+ my_image
    # response['icon_url']
