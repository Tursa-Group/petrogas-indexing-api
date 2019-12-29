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


#relative_path = app/test.pdf

#upload-route
@app.route('/upload_file')
def upload():
    #files and upload_url variables
    files = {'file': open('app/test.pdf','rb')}
    upload_url ='https://api-app.xtracta.com/v1/documents/upload'
    header= {"Content-Type": "application/x-www-form-urlencoded"}

    #auth keys and file to be uploaded
    auth_upload={
        'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
        'workflow_id':'963111',
        'userfile': 'files'
    }

    # POST request to upload pdf file
    r=requests.post(url=upload_url, data=auth_upload, headers=header)
   # return r.text
    return str(r.content)



#/dowload route
@app.route('/download_file/<doc_id>')
def download(doc_id):
    #download url variable
    download_url='https://api-app.xtracta.com/v1/documents/'

    #auth keys and download=document_id
    auth_download={
        'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
        'workflow_id': '963111',
        'document_id': doc_id
    }

    #POST request
    r=requests.post(url=download_url,data=auth_download)
    #return content 
    return str(r.content)
