import os
from flask import render_template, request
from app import app
from PyPDF2 import PdfFileWriter, PdfFileReader
import requests

@app.route('/')
def start():
    return render_template('home.html')

#upload-route
@app.route('/upload', methods = ['POST'])
def upload():
    pdf_data = None 
    xtracta_ids = []  
    if 'pdf' in request.files:
        incoming_pdf = request.files['pdf']
        pdf_data = PdfFileReader(incoming_pdf, 'rb') 
        for i in range(pdf_data.numPages):
            output = PdfFileWriter()
            output.addPage(pdf_data.getPage(i))
            with open("document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)
                print('Created: {}'.format("document-page%s.pdf" % i))
                outputStream.close()
            
            with open("document-page%s.pdf" % i, "rb") as file_to_send:
                files = {'userfile': file_to_send}
                upload_url ='https://api-app.xtracta.com/v1/documents/upload'
                auth_upload = {
                'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
                'workflow_id':'963111'
                }
                r=requests.post(url=upload_url, files=files,data=auth_upload)
                xtracta_ids.append(r.content)
                file_to_send.close()

            os.remove("document-page%s.pdf" % i) 
    else:
        return "please upload a file to process"

    return str(xtracta_ids)

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
