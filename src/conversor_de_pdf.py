from pdf2docx import parse

# Caminho do arquivo PDF original
pdf_arquivo = "documento.pdf"

# Caminho do arquivo Word que será gerado
docx_arquivo = "documento.docx"

# Executa a conversão completa
parse(pdf_arquivo, docx_arquivo)

print("Conversão concluída com sucesso!")
