import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static String[] line = sc.nextLine().split(" ");
    static int N = Integer.parseInt(line[0]);
    static int K = Integer.parseInt(line[1]);
    static int[] words = new int[N];
    static int ans = 0;

    public static void main(String[] args) {
        // read words
        for (int n = 0; n < N; n ++) {
            String word = sc.nextLine();
            int word_bit = 1 << 26;
            for (int i = 0; i < word.length(); i++) {
                word_bit |= 1 << word.charAt(i) - 'a';
            }
            words[n] = word_bit;
        }
        // initialize bits
        int bits = 1 << 26;
        bits |= 1 << 'a'-'a';
        bits |= 1 << 'n'-'a';
        bits |= 1 << 't'-'a';
        bits |= 1 << 'i'-'a';
        bits |= 1 << 'c'-'a';
        int top = -1;
        if (K < 5) {
            System.out.println(0);
        }
        else if (K >= 26) {
            System.out.println(N);
        }
        else {
            bf(5, top, bits);
            System.out.println(ans);
        }
    }
    private static void bf(int k, int top, int bits) {
        if (k == K && ans != N) {  // bf
            int cnt = 0;
            for (int word : words) {
                if ((word | bits) == bits) {
                    cnt ++;
                }
            }
            ans = Math.max(ans, cnt);
        }
        else {
            if (ans == N) {
                return;
            }
            for (int i = top+1; i < 26; i ++) {
                if (i == 0 || i == 13 || i == 19 || i == 8 || i == 2) {
                    continue;
                }
                bf(k+1, i, bits|(1<<i));
            }
        }
    }
}
