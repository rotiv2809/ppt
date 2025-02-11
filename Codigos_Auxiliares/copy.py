from docx import Document

def copy_docx(input_file, output_file):
    # Abrir o documento original
    doc = Document(input_file)
    
    # Salvar uma cópia do documento
    doc.save(output_file)
    print(f'Cópia criada: {output_file}')

