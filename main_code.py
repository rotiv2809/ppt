from Codigos_Auxiliares.teste import split_questions_in_place
from Codigos_Auxiliares.copy import copy_docx
from Codigos_Auxiliares.ppt import pdf_to_ppt
from Codigos_Auxiliares.pdf import convert_to_pdf
from Codigos_Auxiliares.clear import clear_folder
from Codigos_Auxiliares.clear import folders_to_clear
from Google_Drive.puxar_arq import main
from Codigos_Auxiliares.rename import rename_only_file_in_folder
from pathlib import Path
import os

#Limpa todas as pastas antes do download
for folder in folders_to_clear:
    clear_folder(folder)

print("Pastas limpas com sucesso!")

#importando os arquivos do google drive

#IDs das pastas no Google Drive e seus nomes personalizados
folder_data = {
    #"1chJtKUNdd0ip2twLqf42Z6K98EHUuXEY": "capa",
    #"1nxvMceD_5QewLjNMp8YNN2B_XwD8hJk9": "fundo",
    "1CnpMtGRsLEeX58deJmM_dM8-uINNR5-Y": "enunciado"
    #"1kQbWNlo1hpqXixNgxTkf0RpMZcuc6QAC": "gabarito",
    #"15Uhggzy11nmtHXET20lCwfX3yFM4IKHw": "gab_enum"
}

#Baixar arquivos de cada pasta
for folder_id, folder_name in folder_data.items():
    print(f"Baixando arquivos da pasta {folder_name}...")
    main(folder_id, custom_folder_name=folder_name)

#renomear os arquivos para que fique tudo certo

script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path_3 = os.path.join(script_dir,'downloads/enunciado')



rename_only_file_in_folder(folder_path_3,'teste.docx')

# Definição dos caminhos dos arquivos de entrada e saída
input_docx = "downloads/enunciado/teste.docx"
output_docx = "Documentos_Gerados/teste.docx"

# Copia o arquivo original para um novo local
copy_docx(input_docx, output_docx)

# Divide as questões no documento copiado, não no original
split_questions_in_place(output_docx)
print("Questions have been separated by pages")

# Obtém o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos de saída dos arquivos PDF e PPTX
output_pdf = os.path.join(script_dir, 'Documentos_Gerados', 'output.pdf')
output_ppt = os.path.join(script_dir, 'Output', 'output.pptx')

# Converte o documento processado para PDF
convert_to_pdf(output_docx, output_pdf)
print("PDF gerado com sucesso!")

# Converte o PDF gerado em apresentação PowerPoint
pdf_to_ppt(output_pdf, output_ppt)
print("Conversão concluída!")
