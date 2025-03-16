// import java.io.FileInputStream;
// import java.io.PrintStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.PriorityQueue;
import java.util.HashMap;

class Main {

    static int HEAPSIZE = 0;
    static HashMap<Integer, Integer> count = new HashMap<>();

    private static Integer dequeueMin(PriorityQueue<Integer> q) throws Exception {
        // q를 순회하면서 이미 없어져야하는 값이었으면 그걸 없애야함.
        // hashmap을 사용해서 각 숫자의 count를 기록하고, 0 이하가 되면 없어 진거니 삭제하기.
        while (!q.isEmpty()) {
            int top = Integer.parseInt(q.peek().toString());
            // 존재하는 값인 경우에는 poll한 값을 반환
            if (count.containsKey(top) && 0 < count.get(top)) {
                return Integer.parseInt(q.poll().toString());
            }
            // 값이 존재하지 않은 경우. 즉, 업데이트가 안된 경우에는 그냥 poll하고 다음 값을 본다.
            else {
                q.poll();
            }
        }
        throw new Exception("Queue is empty");
    }

    private static Integer dequeueMax(PriorityQueue<Integer> q) throws Exception {
        while (!q.isEmpty()) {
            int top = ~Integer.parseInt(q.peek().toString());
            if (count.containsKey(top) && 0 < count.get(top)) {
                return ~Integer.parseInt(q.poll().toString());
            }
            else {
                q.poll();
            }
        }
        throw new Exception("Queue is empty");
    }

    public static void main(String[] args) throws IOException, Exception {
        // System.setIn(new FileInputStream("input.txt"));
        // System.setOut(new PrintStream("output.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            // initialize max and min heaps
            PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
            PriorityQueue<Integer> minHeap = new PriorityQueue<>();
            int K = Integer.parseInt(br.readLine());

            // 1. 명령 읽고 enqueue, dequeue 수행하기
            for (int k = 0; k < K; k++) {
                String[] line = br.readLine().split(" ");
                String cmd = line[0];
                int value = Integer.parseInt(line[1]);
                // 삽입
                if (cmd.equals("I")) {
                    // heap에 enqueue
                    // priority queue는 기본적으로 min heap.
                    maxHeap.add(~value);
                    minHeap.add(value);
                    // count dictionary, HEAPSIZE 업데이트
                    count.put(value, count.getOrDefault(value, 0) + 1);
                    HEAPSIZE += 1;
                }
                // 삭제
                else {
                    // 비었는지 확인
                    if (HEAPSIZE == 0) {
                        continue;
                    }
                    // 요소가 남아있다면 dequeue 수행.
                    else {
                        int result = (value == 1) ? dequeueMax(maxHeap) : dequeueMin(minHeap);
                        count.put(result, count.get(result) - 1);
                        HEAPSIZE -= 1;
                    } 
                }
            }

            // 2. 정답 출력하기
            // HEAPSIZE == 0 -> 힙에 원소가 없음, EMPTY 출력
            if (HEAPSIZE == 0) {
                System.out.println("EMPTY");
            }
            // HEAP이 비지 않은 경우에
            else {
                // 요소가 하나만 있는 경우 -> 두 힙중 하나에서 dequeue(poll)해서 그 값을 두 번 출력
                if (HEAPSIZE == 1) {
                    int ans = dequeueMax(maxHeap);
                    System.out.printf("%d %d\n", ans, ans);
                }
                // 요소가 두개 이상인 경우 -> 두 힙에서 각각 dequeue(poll)해서 그 값들을 출력
                else {
                    System.out.printf("%d %d\n", dequeueMax(maxHeap), dequeueMin(minHeap));
                }
            }
            
            // count dictionary, HEAPSIZE 초기화
            count.clear();
            HEAPSIZE = 0;
        }
    }
}