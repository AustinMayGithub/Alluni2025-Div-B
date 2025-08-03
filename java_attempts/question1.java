import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class question1 {
    


public static void main(String args[]) {

    Scanner sc = new Scanner(System.in);
    int number = sc.nextInt();
    HashMap<String, Integer> games = new HashMap<>(); 
    for (int i = 0; i < number; i++) {
        String line = sc.nextLine();
        System.out.println(line);

        ArrayList lineArray = new ArrayList<String>();
        lineArray = ArrayList(line.split(" "));
        games.put(lineArray[0], Integer.getInteger(lineArray[1]));
    }
}

}
