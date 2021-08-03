package template_method;

public abstract class Converter
{
    public abstract String readFile(String path);
    public abstract void writeToFile(String path,String data);
    public void createFile(String path)
    {
        System.out.println("Creating File: "+path);
    }
    public void convert(String file,String newFile)
    {
        String data=readFile(file);
        createFile(newFile);
        writeToFile(newFile,data);
    }
}