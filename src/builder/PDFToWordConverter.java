package builder;

public class PDFToWordConverter
{
    private WriteToWordFile writeToWordFile;
    private PDFReader pdfReader;
    private WordFileCreator wordFileCreator;
    public void convert(String pdfFile,String wordFile)
    {
        wordFileCreator.create(wordFile);
        writeToWordFile.write(pdfReader.read(pdfFile),wordFile);
    }
    public WriteToWordFile getWriteToWordFile()
    {
        return writeToWordFile;
    }
    public void setWriteToWordFile(WriteToWordFile writeToWordFile)
    {
        this.writeToWordFile = writeToWordFile;
    }
    public PDFReader getPdfReader()
    {
        return pdfReader;
    }
    public void setPdfReader(PDFReader pdfReader)
    {
        this.pdfReader = pdfReader;
    }
    public WordFileCreator getWordFileCreator()
    {
        return wordFileCreator;
    }
    public void setWordFileCreator(WordFileCreator wordFileCreator)
    {
        this.wordFileCreator = wordFileCreator;
    }
}