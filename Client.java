// A simple Client Server Protocol .. Client for Echo Server
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter; //The Java PrintWriter class ( java. io. PrintWriter ) enables you to write formatted data to an underlying Writer.
import java.net.InetAddress; //class provides methods to get the IP address of any hostname. InetAddress can handle both IPv4 and IPv6 addresses.
import java.net.Socket;

public class Client {

public static void main(String args[]) throws IOException{


    InetAddress address=InetAddress.getLocalHost(); //returns the instance of InetAddress containing local host name and address
    Socket s1=null;
    String line=null;
    BufferedReader br=null;
    BufferedReader is=null;
    PrintWriter os=null;

    try {
        s1=new Socket(address, 4445); // You can use static final constant PORT_NUM
        br= new BufferedReader(new InputStreamReader(System.in));
        is=new BufferedReader(new InputStreamReader(s1.getInputStream()));
        os= new PrintWriter(s1.getOutputStream());
    }
    catch (IOException e){
        e.printStackTrace();
        System.err.print("IO Exception");
    }

    System.out.println("Client Address : "+address);
    System.out.println("Enter Data to echo Server ( Enter QUIT to end):");

    String response=null;
    try{
        line=br.readLine(); 
        while(line.compareTo("QUIT")!=0){
                os.println(line);
                os.flush();
                response=is.readLine();
                System.out.println("Server Response : "+response);
                line=br.readLine();

            }



    }
    catch(IOException e){
        e.printStackTrace();
    System.out.println("Socket read Error");
    }
    finally{

        is.close();os.close();br.close();s1.close();
                System.out.println("Connection Closed");

    }

}
}