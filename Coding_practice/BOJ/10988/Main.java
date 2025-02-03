import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        int wordLength = word.length();
        int s = 0;
        for (int i = 0; i < wordLength; i++) {
            if (word.charAt(i) != word.charAt(wordLength-i-1)){
                System.out.println(0);
                s = 1;
                break;
            }
        }
        if (s != 1){
            System.out.println(1);
        }
    }
}