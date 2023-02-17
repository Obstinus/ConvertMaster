import os
import pdfplumber
import fpdf


class Conversor:
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino

    def converter_pdf_para_txt(self):
        pdf_files = self._obter_arquivos(self.origem, '.pdf')
        for pdf_file in pdf_files:
            with pdfplumber.open(os.path.join(self.origem, pdf_file)) as pdf:
                text = '\nNEWPAGE\n\n'.join(page.extract_text() for page in pdf.pages)
            txt_file = pdf_file.replace('.pdf', '.txt')
            self._salvar_arquivo(os.path.join(self.destino, txt_file), text.strip())

    def converter_txt_para_pdf(self):
        txt_files = self._obter_arquivos(self.origem, '.txt')
        for txt_file in txt_files:
            with open(os.path.join(self.origem, txt_file), 'r', encoding='utf-8', errors='ignore') as infile:
                text = infile.read()
            pdf_file = txt_file.replace('.txt', '.pdf')
            pdf = fpdf.FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(190, 10, txt=text, align='L')
            pdf.output(os.path.join(self.destino, pdf_file))

    def _obter_arquivos(self, diretorio, extensao):
        return [f for f in os.listdir(diretorio) if f.endswith(extensao)]

    def _salvar_arquivo(self, filepath, content):
        with open(filepath, 'w', encoding='utf-8', errors='ignore') as outfile:
            outfile.write(content)


if __name__ == '__main__':
    escolha = input("Quer converter PDF para TXT ou TXT para PDF? (digite 'PDF' ou 'TXT') ")
    origem = input("Qual é o diretório de origem? ")
    destino = input("Qual é o diretório de destino? ")

    if not os.path.isdir(origem):
        print(f"O diretório de origem '{origem}' não existe.")
        exit()
    if not os.path.isdir(destino):
        print(f"O diretório de destino '{destino}' não existe.")
        exit()

    conversor = None
    if escolha.upper() == 'PDF':
        conversor = Conversor(origem, destino)
        conversor.converter_pdf_para_txt()
    elif escolha.upper() == 'TXT':
        conversor = Conversor(origem, destino)
        conversor.converter_txt_para_pdf()
    else:
        print("Escolha inválida. Por favor, digite 'PDF' ou 'TXT'.")
        exit()
