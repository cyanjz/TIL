public class Main2 {
    static int BUFFERSIZE = 1 << 32;
    static int iL = 0;
    static int oL = 0;
    static byte[] input = new byte[BUFFERSIZE];
    static byte[] output = new byte[BUFFERSIZE];
    static int bytesRead = 0;

    public static void main(String[] args) throws Exception{
        bytesRead = System.in.read(input);
        int q = readToken();
        for (int i = 0; i<q; i++) {
            print(readToken() + readToken());
            output[oL++] = (byte)10;
        }
    }
    public static int readToken(){
        int t, a = input[iL++];
        boolean c = false;
        if (a == '-') {
            c = true;
            a = input[iL++];
        }
        a = a&15;
        while ((t = input[iL++]) > 32) {
            a = (a << 3) + (a << 1) + t&15;
        }
        return c? -a:a;
    }
    public static void print(int n) {
        if (oL >= BUFFERSIZE) flush();
        if (n==0) {
            output[oL++] = '0';
            return;
        }
        int startIdx = oL;
        while (n > 0) {
            output[oL++] = (byte) ('0' + (n%10));
            n /= 10;
        }
        for (int i = startIdx, j = oL-1; i<j; i++, j--) {
            byte temp = output[i];
            output[i] = output[j];
            output[j] = temp;
        }
    }
    public static void flush() {
        System.out.write(output, 0, oL);
        System.out.flush();
        oL = 0;
    }
}