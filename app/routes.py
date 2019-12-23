from app import app


@app.route('/')
def start():
    return "I break away from all conventions that do not lead to my earthly success and happiness"


@app.route('/upload')
def upload():
    return "we will upload files here"
    # POST https://api-app.xtracta.com/v1/documents

@app.route('/download')
def download():
    return "this endpoint will receive a doc ID and download its data from xtracta"
    # POST https://api-app.xtracta.com/v1/documents
    