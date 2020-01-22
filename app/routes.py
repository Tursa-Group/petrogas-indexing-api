import os
import json
from flask import render_template, request, jsonify
from app import app
from PyPDF2 import PdfFileWriter, PdfFileReader
import requests

@app.route('/')
def start():
    return render_template('home.html')

#upload odd route
@app.route('/upload', methods = ['POST'])
def upload():
    pdf_data = None 
    xtracta_ids = list()
    if 'pdf' in request.files:
        incoming_pdf = request.files['pdf']
        pdf_data = PdfFileReader(incoming_pdf, 'rb') 
        for i in range(0,pdf_data.numPages,2):
            output.addPage(pdf_data.getPage(i))
            with open("document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)
                print('Created: {}'.format("document-page%s.pdf" % i))
                outputStream.close()
            
            with open("document-page%s.pdf" % i, "rb") as file_to_send:
                print(file_to_send)
                files = {'userfile': file_to_send}
                upload_url ='https://api-app.xtracta.com/v1/documents/upload'
                auth_upload = {
                'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
                'workflow_id':'963111'
                }
                r=requests.post(url=upload_url, files=files,data=auth_upload)
                xtracta_id = r.content[115:124]
                xtracta_ids.append(xtracta_id)
                file_to_send.close()
            with open("document-page%s.pdf" % i, "rb") as pdf_to_upload:
                knack_headers= {
                    'x-knack-rest-api-key': 'ada16490-108d-11ea-a3f2-6365f2950907',
                    'X-Knack-Application-ID': '5ddd46252bd67c0015fa6809'
                }
                knack_files = {'files': pdf_to_upload}
                knack_url = 'https://api.knack.com/v1/applications/5ddd46252bd67c0015fa6809/assets/file/upload'
                knack_r= requests.post(url=knack_url, files=knack_files, headers=knack_headers)
                knack_doc_id =  knack_r.content[7: 31]
                print(knack_doc_id)
                record_url= 'https://api.knack.com/v1/objects/object_4/records'
                record_data= {
                    'field_17': knack_doc_id,
                    'field_41': xtracta_id
                }
                record_r= requests.post(url=record_url, headers=knack_headers, data=record_data)
                print(record_r.content)
                pdf_to_upload.close()

            os.remove("document-page%s.pdf" % i) 
    else:
        return "please upload a file to process" , 403

    return "success"

#upload even route
@app.route('/even-upload', methods = ['POST'])
def even_upload():
    pdf_data = None 
    xtracta_ids = []  
    if 'pdf' in request.files:
        incoming_pdf = request.files['pdf']
        pdf_data = PdfFileReader(incoming_pdf, 'rb') 
        for i in range(1,pdf_data.numPages,2):
            output = PdfFileWriter()
            output.addPage(pdf_data.getPage(i))
            with open("document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)
                print('Created: {}'.format("document-page%s.pdf" % i))
                outputStream.close()
            
            with open("document-page%s.pdf" % i, "rb") as file_to_send:
                #print(file_to_send)
                files = {'userfile': file_to_send}
                upload_url ='https://api-app.xtracta.com/v1/documents/upload'
                auth_upload = {
                'api_key':'b65d6427252e69e4aa29728f6ebfbf43ccf2f266',
                'workflow_id':'963111'
                }
                r=requests.post(url=upload_url, files=files,data=auth_upload)
                xtracta_id = r.content[115:124]
                xtracta_ids.append(xtracta_id)
                file_to_send.close()
            with open("document-page%s.pdf" % i, "rb") as pdf_to_upload:
                knack_headers= {
                    'x-knack-rest-api-key': 'ada16490-108d-11ea-a3f2-6365f2950907',
                    'X-Knack-Application-ID': '5ddd46252bd67c0015fa6809'
                }
                knack_files = {'files': pdf_to_upload}
                knack_url = 'https://api.knack.com/v1/applications/5ddd46252bd67c0015fa6809/assets/file/upload'
                knack_r= requests.post(url=knack_url, files=knack_files, headers=knack_headers)
                knack_doc_id =  knack_r.content[7: 31]
                print(knack_doc_id)
                record_url= 'https://api.knack.com/v1/objects/object_4/records'
                record_data= {
                    'field_17': knack_doc_id,
                    'field_41': xtracta_id
                }
                record_r= requests.post(url=record_url, headers=knack_headers, data=record_data)
                print(record_r.content)
                pdf_to_upload.close()

            os.remove("document-page%s.pdf" % i) 
    else:
        return "please upload a file to process" , 403
    return "success", 200

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
