class WordReader:
    
    def read(self,file):
        print("Reading from ",file)
        return "content"

class PDFWriter:
    
    def write(self,content,file):
        print("Writing to ",file)

class WordPDFConverter:
    
    def __init__(self):
        self.word_reader=WordReader()
        self.pdf_writer=PDFWriter()
    
    def convert(self,word,pdf):
        content=self.word_reader(word)
        self.pdf_writer(content,pdf)