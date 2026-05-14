import java.rmi.*;
import java.rmi.server.*;


public interface Adder extends Remote{

     int add (int x, int y) throws RemoteException;
}