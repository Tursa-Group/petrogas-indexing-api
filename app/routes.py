from app import app
import requests


@app.route('/')
def start():
    return "<h1>Xtracta API </h1> <h4> Created with Flask</h4>"


@app.route('/upload', methods=['POST'])
def upload():
    r=requests.post('https://api-app.xtracta.com/v1/documents/upload')
    return 'posts'
    # POST https://api-app.xtracta.com/v1/documents/upload


    # POST https://api-app.xtracta.com/v1/documents
