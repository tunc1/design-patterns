package mediator;

import java.util.LinkedList;
import java.util.List;

public class ChatRoom
{
    private List<User> users;
    public ChatRoom()
    {
        users=new LinkedList<>();
    }
    public void register(User user)
    {
        users.add(user);
    }
    public void sendMessage(Message message)
    {
        for(User user:users)
        {
            if(!user.equals(message.getSender()))
                user.receiveMessage(message);
        }
    }
}