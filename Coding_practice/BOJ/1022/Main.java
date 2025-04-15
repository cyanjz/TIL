import java.io.FileInputStream;
import java.io.PrintStream;
import java.util.Scanner;


public class Main {
    static int arrSize = 50;
    static int[][] ds = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
    public static void main(String[] args) throws Exception {
        // System.setIn(new FileInputStream("input.txt"));
        // System.setOut(new PrintStream("output.txt"));
        Scanner sc = new Scanner(System.in);
        solve(sc);
    }

    public static void solve(Scanner sc) {
        int[] coordinates = readInput(sc);
        int r1 = coordinates[0];
        int c1 = coordinates[1];
        int r2 = coordinates[2];
        int c2 = coordinates[3];
        // initialize variables
        // 배열 관련 변수
        int row_shift = coordinates[0];
        int col_shift = coordinates[1];
        int[][] arr = new int[r2-r1+1][c2-c1+1];
        int maxNum = 1;
        // 순회 관련 변수
        int cr = 0;
        int cc = 0;
        int cnt = 0;
        int cntEnd = (r2-r1+1) * (c2-c1+1);
        int number = 1;
        int length = 1;
        int dIndex = 0;
        int[] dir = ds[dIndex];
        if (check(cr, cc, r1, r2, c1, c2)) {
            cnt ++;
            arr[cr-row_shift][cc-col_shift] = number;
        }
        while (cnt < cntEnd) {
            // move
            for (int j = 0; j < length; j++) {
                number ++;
                cr += dir[0];
                cc += dir[1];
                if (cnt == cntEnd) {
                    break;
                }
                if (check(cr, cc, r1, r2, c1, c2)) {
                    // System.out.println(number);
                    arr[cr-row_shift][cc-col_shift] = number;
                    maxNum = number;
                    // System.out.println("##########");
                    // printArr(arr, padding, c2-c1);
                    // System.out.println(number);
                    // System.out.printf("%d, %d, %d, %d, %d, %d \n", r1, r2, c1, c2, cr, cc);
                    cnt ++;
                }
            }
            if (cnt == cntEnd) {
                break;
            }
            dIndex = (dIndex + 1) % 4;
            dir = ds[dIndex];
            if (dIndex == 2 || dIndex == 0) {
                length++;
            }
        }
        int padding = getDigit(maxNum);
        printArr(arr, padding, c2-c1);
    }

    public static void printArr(int[][] arr, int padding, int C) {
        for (int[] row : arr) {
            System.out.printf("%"+padding+"d", row[0]);
            for (int c = 1; c <= C; c ++) {
                System.out.printf(" %"+padding+"d", row[c]);
            }
            System.out.print("\n");
        }
    }

    public static int getDigit(int number) {
        int result = 0;
        while (number != 0) {
            number /= 10;
            result += 1;
        }
        return result;
    }

    public static boolean check(int r, int c, int r1, int r2, int c1, int c2) {
        return r1 <= r  && r <= r2 && c1 <= c && c <= c2;
    }

    public static int[] readInput(Scanner sc) {
        String[] line = sc.nextLine().split(" ");
        int[] result = new int[4];
        for (int i = 0; i < 4; i ++) {
            result[i] = Integer.parseInt(line[i]);
        }
        return result;
    }
}
