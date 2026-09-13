package id.ac.usg.sip.model;

@FunctionalInterface
public interface DueDateReminder {
    void remind(String memberName, String title);
}
