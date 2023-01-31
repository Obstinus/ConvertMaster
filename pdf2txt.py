import os
import pdfplumber
import fpdf

def save_file(filepath, content):
    with open (filepath, 'w', encoding='utf-8', errors='ignore') as outfile:
        outfile.write(content)

def convert_pdf2txt(src_dir, dest_dir):
    files = os.listdir(src_dir)
    files = [i for i in files if '.pdf' in i]
    for file in files:
        try:
            with pdfplumber.open(src_dir+file) as pdf:
                output = ''
                for page in pdf.pages:
                    output += page.extract_text()
                    output += '\nNEWPAGE\n\n' # change this for your page demarcation
                save_file(dest_dir+file.replace('.pdf', '.txt'), output.strip())
        except Exception as oops:
            print(oops, file)

def convert_txt2pdf(src_dir, dest_dir):
    files = os.listdir(src_dir)
    files = [i for i in files if '.txt' in i]
    for file in files:
        try:
            with open(src_dir + file, 'r', encoding='utf-8', errors='ignore') as infile:
                text = infile.read()
                pdf = fpdf.FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(190, 10, txt=text, align='L')
                pdf.output(dest_dir + file.replace('.txt', '.pdf'))
        except Exception as oops:
            print(oops, file)

if __name__ == '__main__':
    convert_pdf2txt('/path/to/src/pdf/', '/path/to/dest/txt/')
    convert_txt2pdf('/path/to/src/txt/', '/path/to/dest/pdf/')

