import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;


class Main {
    static int HEAP_SIZE = 100000;
    static int[] heap = new int[HEAP_SIZE];
    static int rear = 0;

    private static int dequeue() {
        // 먼저 루트 노드의 원소를 빼내고
        int root = heap[1];
        // 루트 노드에 rear node의 원소를 할당.
        heap[1] = heap[rear];
        rear -= 1;
        // heapfiy 수행
        heapfiy(1);
        return root;
    }

    private static void heapfiy(int node) {
        int left = 2 * node;
        int right = 2 * node + 1;
        // left가 존재
        if (left <= rear) {
            // right가 존재
            if (right <= rear) {
                if (heap[right] < heap[left] && heap[node] < heap[left]) {
                    int temp = heap[node];
                    heap[node] = heap[left];
                    heap[left] = temp;
                    heapfiy(left);
                } else if (heap[left] <= heap[right] && heap[node] < heap[right]) {
                    int temp = heap[node];
                    heap[node] = heap[right];
                    heap[right] = temp;
                    heapfiy(right);
                }
            }
            // right가 존재 x
            else {
                if (heap[node] < heap[left]) {
                    int temp = heap[node];
                    heap[node] = heap[left];
                    heap[left] = temp;
                    heapfiy(left);
                }
            }
        }
    }

    private static void enqueue(int elem) {
        rear += 1;
        heap[rear] = elem;
        int child = rear;
        int parent = rear / 2;
        while (parent != 0) {
            // child보다 parent가 더 크면 break
            if (heap[parent] > heap[child]) {
                break;
            }
            int temp = heap[parent];
            heap[parent] = heap[child];
            heap[child] = temp;
            child = parent;
            parent /= 2;
        }
    }

    public static void main(String[] args) throws IOException {
        // System.setIn(new FileInputStream("input.txt"));
        // System.setOut(new PrintStream(new FileOutputStream("output.txt")));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().split(" ")[0]);
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine().split(" ")[0]);
            // dequeue
            if (x == 0) {
                // heap이 비어있는 경우
                if (rear == 0) {
                    System.out.println(0);
                }
                // heap이 있는 경우
                else {
                    System.out.println(dequeue());
                }
            }
            else {
                enqueue(x);
            }
            // System.out.println("____loop end____");
            // for (int j = 0; j <= rear; j ++) {
            //     System.out.printf("%d ", heap[j]);
            // }
            // System.out.println();
        }
    }
}