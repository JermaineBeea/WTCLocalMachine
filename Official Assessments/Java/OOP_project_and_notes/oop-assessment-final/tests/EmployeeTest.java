import employees.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class EmployeeTest {
    @Test
    void testManagerDetails() {
        Employee e = new Manager("Alice", 90000, 5);
        assertTrue(e.getDetails().contains("Team Size"));
    }

    @Test
    void testDeveloperDetails() {
        Employee e = new Developer("Bob", 70000, "Java");
        assertTrue(e.getDetails().contains("Language"));
    }

    @Test
    void testInternDetails() {
        Employee e = new Intern("Charlie", 20000, "Alice");
        assertTrue(e.getDetails().contains("Mentor"));
    }
}
