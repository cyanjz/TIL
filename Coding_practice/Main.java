public class Main {
    public static void main(String[] args) {
        Person person1 = new Person("a");
        Person person2 = new Person("b");
        person1.name = "a";
        person2.name = "b";
        System.out.println(person1.name);
        System.out.println(person2.name);
    }
}
class Person {
    public String name;
    public Person(String val) {
        name = val;
    }
    public void print() {
        System.out.println(name);
    }
}
