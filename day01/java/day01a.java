import java.util.*;
import java.io.*;

public class day01a{
    public static void main(String[] args) {
        try{
            System.out.println(new BufferedReader(new FileReader("input01.txt")).lines().map(Integer::parseInt).mapToInt(x -> Math.floorDiv(x, 3)-2).sum());

            BufferedReader br = new BufferedReader(new FileReader("input01.txt"));
            String line;
            int sum = 0;
            while ((line = br.readLine()) != null) {
                sum += Math.floor(Integer.parseInt(line)/3) - 2;
            }
            System.out.println(sum);
        }
        catch(Exception e){
            System.err.println("Åh nej");
        }
    }

}