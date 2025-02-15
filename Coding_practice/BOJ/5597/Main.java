import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> allStudents = new ArrayList<Integer>(30);
        for (Integer i = 0; i < 30; i ++) {
            allStudents.add(i+1);
        }
        for (int i = 0; i < 28; i ++) {
            int studentNumber = Integer.parseInt(br.readLine());
            int idx = allStudents.indexOf(studentNumber);
            allStudents.remove(idx);
        }
        System.out.println(allStudents.get(0));
        System.out.println(allStudents.get(1));
    }
}