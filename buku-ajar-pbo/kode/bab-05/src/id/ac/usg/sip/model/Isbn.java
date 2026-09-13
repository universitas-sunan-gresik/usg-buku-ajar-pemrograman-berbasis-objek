package id.ac.usg.sip.model;

public final class Isbn {
    private final String value;

    public Isbn(String value) {
        String v = value == null ? "" : value.trim();
        if (!v.matches("[0-9-]{10,17}")) {
            throw new IllegalArgumentException(
                "Format ISBN tidak valid: " + value);
        }
        this.value = v;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return value;
    }
}
