class WordReader:
    
    def read(self,file):
        print("Reading from ",file)
        return "content"

class PDFWriter:
    
    def write(self,content,file):
        print("Writing to ",file)

class WordPDFConverter:
    
    def convert(self,word,pdf):
        content=self.word_reader.read(word)
        self.pdf_writer.write(content,pdf)

class WordPDFConverterBuilder:
    
    def __init__(self):
        self.word_pdf_converter=WordPDFConverter()
    
    def build_word_reader(self):
        self.word_pdf_converter.word_reader=WordReader()
    
    def build_pdf_writer(self):
        self.word_pdf_converter.pdf_writer=PDFWriter()
    
    def get_word_pdf_converter(self):
        return self.word_pdf_converter