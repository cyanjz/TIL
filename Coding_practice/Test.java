public class Test{
  public static void main(String[] args){
    int[][] test = new int[3][3];
    for (int r = 0; r < 3; r ++) {
      for (int c = 0; c < 3; c ++) {
        System.out.println(test[r][c]);
      }
    }
  }
}
 
 
class Base{
  int x = 3;
 
  int getX(){
     return x * 2; 
  }
}
 
class Derivate extends Base{
  int x = 7;
  
  int getX(){
     return x * 3;
  }
}
