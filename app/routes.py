from app import app
import requests
import urllib.parse

@app.route('/')
def start():
    return '''
    <!doctype html>
     <title>Xtracta API</title>
      </head>
       <body>
         <h1>Xtracta API</h1>
         <h4>created with Flask</h4>
          <script src="js/scripts.js"></script>
       </body>
    </html>
         '''


@app.route('/upload')
def upload():
    auth_upload={
        'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
        'workflow_id':963111,
        'userfile':''
    }
    upload_url ='https://api-app.xtracta.com/v1/documents/upload'
    r=requests.post(upload_url, data = auth_upload)
    return r.text


#/dowload route 
@app.route('/down-load')
def download():
    auth_download={
        'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
        'workflow_id':963111,
        'document_id':136445044
    }
    download_url='https://api-app.xtracta.com/v1/documents/download'
    r=requests.post(download_url, data = auth_download)

    return str(r.status_code)

# POST https://api-app.xtracta.com/v1/documents
