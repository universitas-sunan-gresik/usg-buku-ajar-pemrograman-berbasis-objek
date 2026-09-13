package id.ac.usg.sip.model;

public class Member {
    String memberId;
    String name;
    String email;
    int maxLoan;

    public Member() {
        this.maxLoan = 3;
    }

    public Member(String memberId, String name,
            String email) {
        this.memberId = memberId;
        this.name = name;
        this.email = email;
        this.maxLoan = 3;
    }

    public String getSummary() {
        return memberId + " - " + name
            + " (maks " + maxLoan + " buku)";
    }

    public boolean canBorrow(int loanCountNow) {
        return loanCountNow < maxLoan;
    }

    public void displayInfo() {
        System.out.println(getSummary());
    }
}
