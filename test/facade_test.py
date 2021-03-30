from unittest import TestCase
from facade import PDFWriter, WordPDFConverter, WordReader
from io import StringIO
import sys

class WordPDFConverterTest(TestCase):

    def test_convert(self):
        stringIO=StringIO()
        sys.stdout=stringIO
        wordPDFConverter=WordPDFConverter()
        word_file="file.docx"
        pdf_file="file.pdf"
        wordPDFConverter.convert(word_file,pdf_file)
        self.assertEquals(stringIO.getvalue(),"Reading from "+word_file+"\nWriting to "+pdf_file+"\n")

class WordReaderTest(TestCase):

    def test_read(self):
        stringIO=StringIO()
        sys.stdout=stringIO
        wordReader=WordReader()
        file="file.docx"
        self.assertEquals(wordReader.read(file),"content")

class PDFWriterTest(TestCase):

    def test_write(self):
        stringIO=StringIO()
        sys.stdout=stringIO
        pdfWriter=PDFWriter()
        file="file.pdf"
        pdfWriter.write("content",file)
        self.assertEquals(stringIO.getvalue(),"Writing to "+file+"\n")