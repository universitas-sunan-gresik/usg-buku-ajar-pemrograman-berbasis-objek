package id.ac.usg.sip.model;

public class Member {
    private String memberId;
    private String name;
    private String email;
    private int maxLoan;

    public Member() {
        this.maxLoan = 3;
    }

    public Member(String memberId, String name,
            String email) {
        setMemberId(memberId);
        this.name = name;
        setEmail(email);
        this.maxLoan = 3;
    }

    public String getMemberId() {
        return memberId;
    }

    public void setMemberId(String memberId) {
        boolean valid = memberId != null
            && memberId.matches("\\d{8}");
        if (!valid) {
            throw new IllegalArgumentException(
                "NIM harus 8 digit: " + memberId);
        }
        this.memberId = memberId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException(
                "Surel tidak valid: " + email);
        }
        this.email = email;
    }

    public int getMaxLoan() {
        return maxLoan;
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
