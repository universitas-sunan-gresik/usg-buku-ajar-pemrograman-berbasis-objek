package id.ac.usg.sip.model;

public class LibraryServiceBad {
    private BookDAOImpl dao = new BookDAOImpl();

    public void processLoan(String itemCode,
            String memberName, String itemType)
            throws Exception {
        Book b = dao.findByCode(itemCode);
        if (b == null) {
            System.out.println("Tidak ditemukan");
            return;
        }
        if (!b.isAvailable()) {
            System.out.println("Tidak tersedia");
            return;
        }
        double denda;
        if (itemType.equals("BOOK")) {
            denda = 500;
        } else if (itemType.equals("JOURNAL")) {
            denda = 300;
        } else {
            denda = 0;
        }
        b.borrow();
        dao.update(b);
        System.out.println(memberName
            + " pinjam " + b.getTitle()
            + ", denda/hari Rp" + denda);
    }
}
