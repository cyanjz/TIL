public class Test{
  public static void main(String[] args){
    Base a =  new Derivate();
    Derivate b = new Derivate();
    
    System.out.println(a.getX() + a.x + b.getX() + b.x);
    System.out.println(a.x);
    System.out.println(a.getX());
    System.out.println(b.x);
    System.out.println(b.getX());
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
