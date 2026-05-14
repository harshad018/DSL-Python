import java.rmi.*;
import java.rmi.server.*;

public class AdderRemote extends UnicastRemoteObject implements Adder{


    AdderRemote() throws RemoteException{

        super();
    }

    public int add (int x , int y) throws RemoteException{

        System.out.println("client requeststed: " + x + " + " + y);

        return ( x + y);
    }
}