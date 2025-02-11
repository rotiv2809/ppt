import os
import shutil

# Função para limpar os arquivos de uma pasta
def clear_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove arquivo ou link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove subpasta
            except Exception as e:
                print(f"Erro ao deletar {file_path}: {e}")
    else:
        print(f"A pasta {folder_path} não existe. Criando-a...")
        os.makedirs(folder_path)

# Pastas que precisam ser limpas
script_dir = os.path.dirname(os.path.abspath(__file__))
folders_to_clear = [
    # os.path.join(script_dir, 'downloads/capa'),
    # os.path.join(script_dir, 'downloads/fundo'),
    os.path.join(script_dir, 'downloads/enunciado'),
    # os.path.join(script_dir, 'downloads/gabarito'),
    # os.path.join(script_dir, 'downloads/gab_enum'),
]
