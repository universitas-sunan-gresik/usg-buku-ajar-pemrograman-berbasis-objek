package id.ac.usg.sip.model;

public class AksesModel {
    private String rahasia = "hanya kelas ini";
    String sepaket = "sekelas & sepaket";
    protected String turunan = "sepaket & subclass";
    public String publik = "semua kelas";

    public void tampilkanSemua() {
        System.out.println("private   : " + rahasia);
        System.out.println("default   : " + sepaket);
        System.out.println("protected : " + turunan);
        System.out.println("public    : " + publik);
    }
}
