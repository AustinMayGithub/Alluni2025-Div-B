import java.util.ArrayList;
import java.util.Scanner;

public class questionB {
    
    public static void main(String args[]) 
    {

    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    ArrayList giveList = new ArrayList<String>(n);
    ArrayList recList = new ArrayList<String>(n);

    for (int i = 0; i < n; i++)
    {
        giveList.add(sc.next());
        recList.add(sc.next());
    }

    for (int i = 0; i < n; i++)
    {
        if (giveList.contains(recList[i]))
        

    }

    }
}
