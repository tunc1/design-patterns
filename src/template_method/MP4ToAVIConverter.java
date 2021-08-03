package template_method;

public class MP4ToAVIConverter extends Converter
{
    public String readFile(String path)
    {
        System.out.println("Reading From MP4 File: "+path);
        return "Data";
    }
    public void writeToFile(String path, String data)
    {
        System.out.println("Writing To AVI File: "+path);
    }
}