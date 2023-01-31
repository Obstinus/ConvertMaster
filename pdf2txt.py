import os
import pdfplumber

def save_file(filepath, content):
    with open (filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def convert_pdf2txt(src_dir, dest_dir):
    if not os.path.isdir(src_dir) or not os.path.isdir(dest_dir):
        raise Exception("Directory not found")
    
    files = [f for f in os.listdir(src_dir) if f.endswith('.pdf')]
    for file in files:
        src_file = os.path.join(src_dir, file)
        dest_file = os.path.join(dest_dir, os.path.splitext(file)[0] + '.txt')
        if os.path.isfile(dest_file):
            raise Exception(f"File {dest_file} already exists")
        
        try:
            with pdfplumber.open(src_file) as pdf:
                output = ''
                for page in pdf.pages:
                    output += page.extract_text()
                    output += '\n'
                save_file(dest_file, output.strip())
        except Exception as oops:
            print(f"An error occured while processing {src_file}: {oops}")

if __name__ == '__main__':
    src_dir = os.path.expanduser('~/Documents/PDFConv/PDFs/')
    dest_dir = os.path.expanduser('~/Documents/PDFConv/Converted/')
    convert_pdf2txt(src_dir, dest_dir)
