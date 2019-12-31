from flask import render_template, request
from app import app
import requests


@app.route('/')
def start():
    return render_template('home.html')


#upload-route
@app.route('/upload')
def upload():
    #files and upload_url variables
    files = {'userfile': open('test2.pdf','rb')}
    upload_url ='https://api-app.xtracta.com/v1/documents/upload'
    
    #auth keys and file to be uploaded
    auth_upload={
        'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
        'workflow_id':'963111'
    }
    

    # POST request to upload pdf file
    r=requests.post(url=upload_url, files=files,data=auth_upload)
   
   # return r.content
    return r.content   


#/dowload route
@app.route('/download/<doc_id>')
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
    
    return r.content
