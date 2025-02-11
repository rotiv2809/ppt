import os
from pathlib import Path
import win32com.client as win32

def convert_to_pdf(word_file, pdf_output):
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(word_file):
        print(f"Erro: O arquivo Word não foi encontrado em: {word_file}")
        return

    try:
        # Inicializa o Word
        word_app = win32.gencache.EnsureDispatch("Word.Application")
        word_app.Visible = False  # Oculta o Word
        doc = word_app.Documents.Open(os.path.abspath(word_file))

        # Obtém o diretório da saída e cria se não existir
        output_dir = Path(pdf_output).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Salva o documento como PDF
        doc.ExportAsFixedFormat(
            OutputFileName=str(pdf_output),
            ExportFormat=17,  # 17 é o valor para PDF
            OpenAfterExport=False
        )
        print(f"Documento salvo como PDF em: {pdf_output}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fecha o documento e o Word corretamente
        try:
            doc.Close(SaveChanges=False)
        except Exception as e:
            print(f"Erro ao fechar o documento: {e}")
        word_app.Quit()
