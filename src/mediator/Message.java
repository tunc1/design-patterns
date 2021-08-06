package mediator;

public class Message
{
    private final User sender;
    private final String message;
    public Message(User sender, String message)
    {
        this.sender = sender;
        this.message = message;
    }
    public User getSender()
    {
        return sender;
    }
    public String getMessage()
    {
        return message;
    }
}