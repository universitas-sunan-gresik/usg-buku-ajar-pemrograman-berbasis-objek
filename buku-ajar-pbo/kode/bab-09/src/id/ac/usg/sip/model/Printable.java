package id.ac.usg.sip.model;

public interface Printable {
    String getSummary();

    default void printLabel() {
        System.out.println("=== LABEL RAK ===");
        System.out.println(getSummary());
        System.out.println("=================");
    }

    static String formatCode(String code) {
        return "[" + code.toUpperCase() + "]";
    }
}
