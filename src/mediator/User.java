package mediator;

public class User
{
    private final ChatRoom chatRoom;
    private final String username;
    public User(ChatRoom chatRoom, String username)
    {
        this.chatRoom = chatRoom;
        this.username = username;
        chatRoom.register(this);
    }
    public void sendMessage(String message)
    {
        chatRoom.sendMessage(new Message(this, message));
    }
    public void receiveMessage(Message message)
    {
        System.out.println("User "+username+" Received Message: "+message.getMessage()+" From User "+message.getSender().getUsername());
    }
    public String getUsername()
    {
        return username;
    }
}