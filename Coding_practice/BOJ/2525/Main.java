import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static String calculateTime (int hc, int mc, int duration) {
        int endH = duration/60 + hc;
        int endM = duration%60 + mc;
        return String.format("%d %d", (endH+endM/60)%24, endM%60);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] timeCurrent = br.readLine().split(" ");
        int hourCurrent = Integer.parseInt(timeCurrent[0]);
        int minCurrent = Integer.parseInt(timeCurrent[1]);
        int duration = Integer.parseInt(br.readLine());
        System.out.println(calculateTime(hourCurrent, minCurrent, duration));
    }
}