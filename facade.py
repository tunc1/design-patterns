class WordReader:
    
    def read(self,file):
        return "content"

class PDFWriter:
    
    def write(self,content,file):
        print("Writing to",file)

class WordPDFConverter:
    
    def __init__(self):
        self.word_reader=WordReader()
        self.pdf_writer=PDFWriter()
    
    def convert(self,word,pdf):
        content=self.word_reader.read(word)
        print("Reading from",word)
        self.pdf_writer.write(content,pdf)