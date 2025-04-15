import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split(" ");
        long W = Long.parseLong(line[0]);
        long H = Long.parseLong(line[1]);
        int f = Integer.parseInt(line[2]);
        int c = Integer.parseInt(line[3]);
        int x1 = Integer.parseInt(line[4]);
        int y1 = Integer.parseInt(line[5]);
        int x2 = Integer.parseInt(line[6]);
        int y2 = Integer.parseInt(line[7]);
        
        long h =  (f >= W-f) ? W-f : f;

        long left = 0;
        long right = 0;
        if (x1 < h && h < x2) {
            left = (h >= x1) ? h-x1 : 0;
            right = (x2 >= h) ? x2-h : 0;
        }
        else if (h >= x2) {
            left = (x2-x1);
            right = 0;
        }
        else {
            left = 0;
            right = (x2-x1);
        }

        long ans = W*H - (left*2*(c+1)+right*(c+1))*(y2-y1);
        System.out.println(ans);
    }
}
