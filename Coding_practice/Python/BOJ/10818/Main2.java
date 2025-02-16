public class Main2 {
    static int BUFFERSIZE = 1<<23;
    static int l = 0;
    static byte[] buffer = new byte[BUFFERSIZE];
    public static void main(String[] args) throws Exception {
        System.in.read(buffer);
        int N = r();
        int number = r(), maximum = number, minimum = number;
        for (int i = 1; i < N; i ++) {
            number = r();
            if (number > maximum) maximum = number;
            else if (minimum > number) minimum = number;
        }
        System.out.printf("%d %d", minimum, maximum);
    }
    static int r(){
        int t, a = buffer[l++];
        boolean c = false;
        if (a == '-') {
            c = true;
            a = buffer[l++];
        }
        a = a&15;
        while((t = buffer[l++]) > 32){
            a = (a<<3) + (a<<1) + (t&15);
        }
        return c ? -a:a;
    }
}