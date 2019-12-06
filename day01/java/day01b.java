import java.util.*;
import java.io.*;

public class day01b{
    public static void main(String[] args) {
        try{
            BufferedReader br = new BufferedReader(new FileReader("input01.txt"));
            String line;
            int sum = 0;

            while ((line = br.readLine()) != null) {
                int l = Math.floorDiv(Integer.parseInt(line), 3) - 2;
                while(l > 0){
                    if(l > 0){
                       sum += l; 
                    }
                    l = Math.floorDiv(l,3) - 2;
                }
            }
            System.out.println(sum);
        }
        catch(Exception e){
            System.err.println("Åh nej");
        }
    }
}