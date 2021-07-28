package facade;

public class PDFToWordConverter
{
    private WriteToWordFile writeToWordFile;
    private PDFReader pdfReader;
    private WordFileCreator wordFileCreator;
    public PDFToWordConverter()
    {
        writeToWordFile=new WriteToWordFile();
        pdfReader=new PDFReader();
        wordFileCreator=new WordFileCreator();
    }
    public void convert(String pdfFile,String wordFile)
    {
        wordFileCreator.create(wordFile);
        writeToWordFile.write(pdfReader.read(pdfFile),wordFile);
    }
}