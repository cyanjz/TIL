import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int L = Integer.parseInt(line[1]);
        int[] ans = solve(N, L);
        for (int i = ans[0]; i < ans[0]+ans[1]; i++) {
            System.out.printf("%d ", i);
        }
    }

    public static int[] solve(int N, int L) {
        int length = L;
        while (length <= 100) {
            int start = (2*N-length*length+length)/(2*length);
            int is_availabe = (2*N-length*length+length)%(2*length);
            if (start >= 0 && is_availabe == 0) {
                int[] result = {start, length};
                return result;
            }
            length++;
        }
        int[] result = {-1, 1};
        return result;
    }
}
