A forma mais rápida e eficiente de converter um arquivo PDF para Word (`.docx`) em Python mantendo a formatação original é utilizando a biblioteca **`pdf2docx`**. 

Abaixo está o passo a passo direto para instalar e rodar o script.

## **1\. Instalação da biblioteca**

Abra o seu terminal ou prompt de comando e execute: \[3\]

pip install pdf2docx

## **2\. Código Python para conversão**

O método **`parse`** permite converter o documento inteiro de forma simples com apenas uma linha de código:

from pdf2docx import parse

*\# Caminho do arquivo PDF original*

pdf\_arquivo \= "documento.pdf"

*\# Caminho do arquivo Word que será gerado*

docx\_arquivo \= "documento.docx"

*\# Executa a conversão completa*

parse(pdf\_arquivo, docx\_arquivo)

print("Conversão concluída com sucesso\!")

## 3\. Converter apenas páginas específicas (Opcional)

Se o PDF for muito grande e você precisar extrair apenas um trecho, use os parâmetros `start` (página inicial) e `end` (página final, não inclusiva): \[4\]

from pdf2docx import parse

pdf\_arquivo \= "documento.pdf"

docx\_arquivo \= "paginas\_selecionadas.docx"

*\# Converte apenas da página 1 até a página 5*

parse(pdf\_arquivo, docx\_arquivo, start=0, end=5)

## 📌 Limitação Importante

* **PDFs Escaneados:** Esta biblioteca funciona extraindo os elementos de texto e tabelas digitais. Caso o seu PDF seja gerado a partir de uma foto ou scanner (sem texto selecionável), os métodos acima criarão um Word apenas com imagens coladas. Para resolver isso, seria necessário aplicar uma ferramenta de **OCR** (Reconhecimento Óptico de Caracteres), como o `pytesseract`. 

