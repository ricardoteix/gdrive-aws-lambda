import base64
from email import message_from_string
import json
import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
import re
import datetime
import os


GOOGLE_FOLDER_ID = os.environ.get('GOOGLE_FOLDER_ID')
GOOGLE_CREDENTIALS = os.environ.get('GOOGLE_CREDENTIALS')
PASSWORD = os.environ.get('PASSWORD')

# Função para autenticar com o Google Drive
def authenticate_with_google():
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS, scopes=['https://www.googleapis.com/auth/drive.file']
    )
    service = build('drive', 'v3', credentials=credentials)
    return service

def send_file_post(event):
    
    try:
        
        now = datetime.datetime(2020, 8, 27, 4, 16, 33)
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

        # O corpo da requisição será um arquivo binário (não Base64)
        file_content_base64 = event['body']
        file_name = event['headers'].get('filename', f'arquivo_desconhecido_{timestamp}.bin')
        file_passwd = event['headers'].get('passwd', '')

        _, file_extension = os.path.splitext(file_name)

        print(file_name, file_extension)

        mimetypes = {
            '.pdf': 'application/pdf',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.zip': 'application/zip',
            '.docx': 'application/msword',
            '.doc': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.xml': 'application/xml',
            '.bin': 'application/octet-stream',
            'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'zip': 'application/x-zip-compressed'
        }

        if file_passwd != PASSWORD:
            return {
                'statusCode': 401,
                'body': 'Acesso negado'
            }

        # Verificar se o conteúdo foi enviado em Base64 ou não
        if event.get('isBase64Encoded', False):
            # O conteúdo está codificado em Base64, então decodificamos
            file_content = base64.b64decode(file_content_base64)
        else:
            # Se não estiver codificado, assumimos que é um arquivo binário
            file_content = file_content_base64.encode('utf-8')  # Apenas para garantir que seja tratado como binário

        # Autenticar com o Google Drive
        service = authenticate_with_google()

        # Definindo os metadados do arquivo
        file_metadata = {
            'name': file_name,
            'parents': [GOOGLE_FOLDER_ID]  # Substitua com o ID da pasta correta
        }

        # Criando o arquivo para upload
        media = MediaIoBaseUpload(BytesIO(file_content), mimetype=mimetypes[file_extension])  # Ajuste o mimetype conforme necessário

        # Enviando o arquivo para o Google Drive
        request = service.files().create(media_body=media, body=file_metadata)
        file = request.execute()

        return {
            'statusCode': 200,
            'body': f'Arquivo {file_name} enviado para o Google Drive com sucesso!'
        }

    except Exception as e:
        print(f'Erro ao processar o arquivo: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Erro ao processar o arquivo: {str(e)}'
        }

def show_site_get(lambda_url):
    html_content = """
        <h1>Não foi possível processar sua solicitação.</h1>
    """
    with open("index.html", "r") as f:
        html_content = f.read()

    html_content = html_content.replace('LAMBDA_FUNCTION', lambda_url)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_content
    }

def lambda_handler(event, context):
    
    host = event['headers'].get('host')
    lambda_url = f"https://{host}"

    method = 'GET'

    try:
        method = event['requestContext']['http']['method']
    except Exception as e:
        print(f'Erro ao processar requestContext: {str(e)}')
    
    if method == 'POST':
        return send_file_post(event)
    
    return show_site_get(lambda_url)

