class Parent {
  // 부모 클래스의 생성자
  Parent() {
      System.out.println("Parent class constructor called");
  }
}

class Child extends Parent {
  // 자식 클래스의 생성자
  Child() {
      // 부모 클래스의 생성자가 자동으로 먼저 호출됩니다.
      System.out.println("Child class constructor called");
  }
}

public class Main {
  public static void main(String[] args) {
      // Child 클래스의 객체를 생성하면
      // 부모 클래스 생성자 -> 자식 클래스 생성자 순으로 호출됩니다.
      Child child = new Child();
  }
}
