from app import app
import requests


@app.route('/')
def start():
    return "<h1>Xtracta API <h2(created with FLASK)/></h1>"


@app.route('/upload', methods=['POST'])
def upload():
    r = requests.post('https://api-app.xtracta.com/v1/documents/upload')
    return r.json()
    # POST https://api-app.xtracta.com/v1/documents/upload


@app.route('/download/', methods=['POST'])
def download():
    r = requests.post('https://api-app.xtracta.com/v1/documents')
    return r.json()
    # POST https://api-app.xtracta.com/v1/documents
