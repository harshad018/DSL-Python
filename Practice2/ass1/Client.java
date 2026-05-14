import java.rmi.*;

import java.util.*;

public class Client{


    public static void main(String[] args){


        try{


            Adder stub = (Adder)Naming.lookup("rmi://localhost:1099/AddService");


            Scanner scan = new Scanner(System.in);

            System.out.println("Enter the first number: ");
            int a = scan.nextInt();

            System.out.println("Enter the second number: ");
            int b = scan.nextInt();

            System.out.println("Result is: " + stub.add(a,b));
        }catch(Exception e){

            System.out.println(e);
        }
    }
}