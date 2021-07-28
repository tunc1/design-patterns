package builder;

public class PDFToWordConverterBuilder
{
    private PDFToWordConverter pdfToWordConverter;
    public PDFToWordConverterBuilder()
    {
        pdfToWordConverter=new PDFToWordConverter();
    }
    public void buildPDFReader()
    {
        pdfToWordConverter.setPdfReader(new PDFReader());
    }
    public void buildWordFileCreator()
    {
        pdfToWordConverter.setWordFileCreator(new WordFileCreator());
    }
    public void buildWriteToWordFile()
    {
        pdfToWordConverter.setWriteToWordFile(new WriteToWordFile());
    }
    public PDFToWordConverter getPdfToWordConverter()
    {
        return pdfToWordConverter;
    }
}