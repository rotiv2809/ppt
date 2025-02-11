from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
import io
import os
from datetime import datetime

# Função para autenticar no Google Drive
def authenticate_google_drive():
    # Obtenha o diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho para o arquivo credentials.json
    credentials_path = os.path.join(script_dir, 'credentials.json')
    
    # Carregar as credenciais
    creds = Credentials.from_service_account_file(credentials_path)
    
    return build('drive', 'v3', credentials=creds)

# Função para listar arquivos em uma pasta específica
def list_files_in_folder(service, folder_id):
    results = service.files().list(
        q=f"'{folder_id}' in parents",  # Filtra arquivos pela pasta
        spaces='drive',
        fields="files(id, name)"
    ).execute()
    return results.get('files', [])

# Função para fazer download de um arquivo
def download_file(service, file_id, destination):
    request = service.files().get_media(fileId=file_id)
    with io.FileIO(destination, 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}% concluído.")
    print(f"Arquivo baixado: {destination}")

# Função principal
def main(folder_id, custom_folder_name=None):
    # Autenticação
    service = authenticate_google_drive()

    # Listar arquivos na pasta
    print("Listando arquivos na pasta...")
    files = list_files_in_folder(service, folder_id)

    if not files:
        print("Nenhum arquivo encontrado na pasta.")
        return

    # Criar uma pasta local personalizada
    base_folder = "downloads"
    os.makedirs(base_folder, exist_ok=True)

    # Nome personalizado da pasta
    if not custom_folder_name:
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        custom_folder_name = f"download_{current_datetime}"
    
    full_path = os.path.join(base_folder, custom_folder_name)
    os.makedirs(full_path, exist_ok=True)

    # Baixar todos os arquivos da pasta
    for file in files:
        file_name = file['name']
        file_id = file['id']
        print(f"Baixando arquivo: {file_name}...")
        download_file(service, file_id, os.path.join(full_path, file_name))

    print(f"Todos os arquivos foram baixados com sucesso na pasta: {full_path}")

# Executar o programa
if __name__ == "__main__":
    # IDs das pastas no Google Drive e seus nomes personalizados
    folder_data = {
        "1chJtKUNdd0ip2twLqf42Z6K98EHUuXEY": "capa",
        "1nxvMceD_5QewLjNMp8YNN2B_XwD8hJk9": "fundo",
        "1CnpMtGRsLEeX58deJmM_dM8-uINNR5-Y": "enunciado",
        "1kQbWNlo1hpqXixNgxTkf0RpMZcuc6QAC": "gabarito"
    }

    # Baixar arquivos de cada pasta
    for folder_id, folder_name in folder_data.items():
        print(f"Baixando arquivos da pasta {folder_name}...")
        main(folder_id, custom_folder_name=folder_name)


