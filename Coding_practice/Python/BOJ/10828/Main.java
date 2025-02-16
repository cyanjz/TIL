import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> st = new Stack<>();
        for (int n=0; n<N; n++){
            String[] cmd = br.readLine().split(" ");
            if (cmd[0] == "push") st.push(Integer.parseInt(cmd[1]));
            else if (cmd[0].equals("pop")) System.out.println(st.pop());
            else if (cmd[0].equals("size")) System.out.println(st.size());
            else if (cmd[0].equals("empty")) System.out.println(st.empty());
            else if (cmd[0].equals("top")) System.out.println(st.peek());
        }
    }
}
