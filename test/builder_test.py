from unittest import TestCase
from builder import WordPDFConverterBuilder

class WordPDFConverterBuilderTest(TestCase):

    def setUp(self):
        self.builder=WordPDFConverterBuilder()
    
    def test_build_word_reader(self):
        self.builder.build_word_reader()
        converter=self.builder.get_word_pdf_converter()
        self.assertIsNotNone(converter.word_reader)
    
    def test_build_pdf_writer(self):
        self.builder.build_pdf_writer()
        converter=self.builder.get_word_pdf_converter()
        self.assertIsNotNone(converter.pdf_writer)