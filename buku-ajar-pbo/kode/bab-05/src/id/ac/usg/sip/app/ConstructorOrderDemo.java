package id.ac.usg.sip.app;

public class ConstructorOrderDemo {
    static class Induk {
        Induk() {
            System.out.println(
                "1. Constructor Induk");
        }
    }

    static class Turunan extends Induk {
        Turunan() {
            System.out.println(
                "2. Constructor Turunan");
        }
    }

    public static void main(String[] args) {
        new Turunan();
    }
}
