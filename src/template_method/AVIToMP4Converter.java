package template_method;

public class AVIToMP4Converter extends Converter
{
    public String readFile(String path)
    {
        System.out.println("Reading From AVI File: "+path);
        return "Data";
    }
    public void writeToFile(String path, String data)
    {
        System.out.println("Writing To MP4 File: "+path);
    }
}