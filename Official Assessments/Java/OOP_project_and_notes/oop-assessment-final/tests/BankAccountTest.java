import bank.BankAccount;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BankAccountTest {
    @Test
    void testDeposit() {
        BankAccount acc = new BankAccount("123", "Alice", 100);
        acc.deposit(50);
        assertEquals(150, acc.getBalance());
    }

    @Test
    void testWithdrawSuccess() {
        BankAccount acc = new BankAccount("123", "Alice", 100);
        acc.withdraw(40);
        assertEquals(60, acc.getBalance());
    }

    @Test
    void testWithdrawFailure() {
        BankAccount acc = new BankAccount("123", "Alice", 100);
        acc.withdraw(200);
        assertEquals(100, acc.getBalance(), "Balance should remain unchanged");
    }
}
