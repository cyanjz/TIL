// 그리디 알고리즘 구상
// 1. 먼저 가장 멀리 있는 책을 한번만 가는게 좋아보인다.
// 가장 멀리 있는 책을 구하고, 그 책과 가장 가까운 M개의 책을 제자리에 놓을 때 한번만 가는게 좋다.
// 2. 나머지 책들을 반환하는 규칙은 어떻게 해야할까?
// 멀리 있는 책을 반환하면서 가장 가까이 있는 책들을 같이 가져가는게 좋다.
// [3, 4, 10, 11] 이렇게 책이 놓여야할 위치가 정해져 있고 M =2라면, 11을 반환할 때는 10, 11을 가지고 가서
// 한번에 반환하고 돌아오는게 좋다.
// 3. 양수와 음수를 같이 가져가는 것은 의미가 없다.
// 만약에 -2, 6책을 가지고 반납하러 간다면, 2 * 2 + 6 * 2 = 16만큼의 거리를 이동해야한다.
// 따라서 -2만 가지고 가서 반납한 뒤에 6만 가지고 가서 반납하는 것과 동일하다.
// 양수와 음수부를 나눠서 생각하는게 좋겠다.

// 알고리즘 구상
// 1. 자료 구조
// 먼저 배열을 양수부와 음수부로 나누고, 음수부는 절대값을 씌운다.
// 이후 두 배열을 정렬한다.
// 2. 탐색 시작
// 양수와 음수 둘 중에 하나가 없다면, 존재하는 쪽에서 최댓값을 찾고 그로부터 가까운 M개의 책을 마지막에 반납.
// 양수와 음수 둘다 있다면, 양수의 최댓값과 음수의 최댓값을 비교하여 더 큰 방향에서 M개의 책을 마지막에 반납.
// 반납하는 과정에서 거리를 계산하기.
import java.util.Arrays;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileInputStream;
import java.io.PrintStream;


class Main {
    static BufferedReader br;
    static String[] line;
    static int N, M;
    static String[] temp;
    static {
        try {
            // System.setIn(new FileInputStream("input.txt"));
            // System.setOut(new PrintStream("output.txt"));
            br = new BufferedReader(new InputStreamReader(System.in));
            line = br.readLine().split(" ");
            N = Integer.parseInt(line[0]);
            M = Integer.parseInt(line[1]);
            temp = br.readLine().split(" ");
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static int getStep(int[] arr, int flag) {
        int lenArr = arr.length;
        int idx = lenArr - 1;
        int ans = 0;
        if (flag == 1) {
            ans += arr[idx];
            idx -= M;
        }
        while (idx >= 0) {
            ans += arr[idx]*2;
            idx -= M;
        }
        return ans;
    }
    public static void main(String[] args) {
        // 1. 입력값을 받고, 해당 배열을 양수부와 음수부로 나눈다.
        int[] pos = new int[N];
        int posTop = -1;
        int[] neg = new int[N];
        int negTop = -1;
        for (int i = 0; i < N; i ++) {
            int num = Integer.parseInt(temp[i]);
            if (num > 0) {
                posTop += 1;
                pos[posTop] = num;
            }
            else {
                negTop += 1;
                neg[negTop] = -num;
            }
        }
        Arrays.sort(pos);
        Arrays.sort(neg);
        // 2. 양수가 없는 경우, 음수가 없는 경우, 양수와 음수 둘 다 있는 경우.
        if (posTop == -1) {
            System.out.println(getStep(neg, 1));
        }
        else if (negTop == -1) {
            System.out.println(getStep(pos, 1));
        }
        else {
            int posMax = pos[pos.length-1];
            int negMax = neg[neg.length-1];
            if (posMax > negMax) {
                System.out.println(getStep(pos, 1)+getStep(neg, 0));
            }
            else {
                System.out.println(getStep(neg, 1)+getStep(pos, 0));
            }
        }
    }
}