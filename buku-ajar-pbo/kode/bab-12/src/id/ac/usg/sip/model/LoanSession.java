package id.ac.usg.sip.model;

public class LoanSession implements AutoCloseable {
    private String memberName;

    public LoanSession(String memberName) {
        this.memberName = memberName;
        System.out.println(
            "Sesi dibuka: " + memberName);
    }

    public void process() {
        System.out.println("Memproses peminjaman");
    }

    @Override
    public void close() {
        System.out.println(
            "Sesi ditutup: " + memberName);
    }
}
