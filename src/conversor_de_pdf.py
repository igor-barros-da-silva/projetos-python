from pathlib import Path
from pdf2docx import parse

# Importa pathlib para trabalhar com caminhos de arquivo de forma segura
# Importa a função parse do pdf2docx para fazer a conversão PDF -> DOCX

def converter_pdf_para_docx(pdf_caminho: Path, docx_caminho: Path) -> None:
    """Converte um arquivo PDF em um arquivo DOCX."""
    # Verifica se o arquivo PDF existe antes de tentar converter
    if not pdf_caminho.exists():
        raise FileNotFoundError(f"Arquivo PDF não encontrado: {pdf_caminho}")

    # Executa a conversão passando os caminhos como strings
    parse(str(pdf_caminho), str(docx_caminho))


def main() -> None:
    # Define a pasta base do projeto a partir do local deste arquivo
    base = Path(__file__).resolve().parent.parent

    # Define o caminho do PDF de entrada e do DOCX de saída
    pdf_arquivo = base / "data" / "documento.pdf"
    docx_arquivo = base / "documento.docx"

    # Tenta converter o PDF e informa o resultado ao usuário
    try:
        converter_pdf_para_docx(pdf_arquivo, docx_arquivo)
        print(f"Conversão concluída com sucesso! Arquivo gerado em: {docx_arquivo}")
    except Exception as error:
        # Se ocorrer qualquer erro, exibe uma mensagem de erro
        print(f"Erro ao converter o PDF: {error}")


# Executa a função main apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()
