import java.rmi.*;
import java.rmi.registry.*;


public class Server{


    public static void main(String[] args) {



        try{


            AdderRemote obj = new AdderRemote();

            LocateRegistry.createRegistry(1099);

            Naming.rebind("rmi://localhost:1099/AddService",obj);

            System.out.println("Server is running....");


        }catch(Exception e){

            System.out.println(e);
        }
    }
}