import os
from pathlib import Path

def rename_only_file_in_folder(folder_path, new_name):
    """
    Renomeia o único arquivo na pasta especificada para um novo nome.
    :param folder_path: Caminho da pasta onde está o arquivo.
    :param new_name: Novo nome para o arquivo (incluindo extensão).
    """
    folder = Path(folder_path)
    files = list(folder.iterdir())  # Obtém todos os itens na pasta

    # Filtrar apenas arquivos
    files = [file for file in files if file.is_file()]

    if len(files) == 0:
        raise FileNotFoundError(f"Nenhum arquivo encontrado na pasta: {folder_path}")
    elif len(files) > 1:
        raise Exception(f"Mais de um arquivo encontrado na pasta: {folder_path}")

    # Renomear o único arquivo
    old_file = files[0]
    new_file = folder / new_name
    old_file.rename(new_file)

    print(f"Arquivo renomeado de {old_file.name} para {new_name}")
    return new_file

# Exemplo de uso
if __name__ == "__main__":
    # Caminho da pasta onde o único arquivo está localizado
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir,'downloads/capa')

    # Novo nome para o arquivo
    new_name = "capa_novo.pdf"

    try:
        renamed_file = rename_only_file_in_folder(folder_path, new_name)
        print(f"Arquivo foi renomeado com sucesso para: {renamed_file}")
    except Exception as e:
        print(f"Erro: {e}")
