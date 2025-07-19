```java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class UserServiceTest {

    private UserService userService;

    @BeforeEach
    public void setUp() {
        userService = new UserService();
    }

    @Test
    public void testIsValidUser_NullUsername() {
        assertFalse(userService.isValidUser(null), "Expected false for null username");
    }

    @Test
    public void testIsValidUser_EmptyUsername() {
        assertFalse(userService.isValidUser(""), "Expected false for empty username");
    }

    @Test
    public void testIsValidUser_ShortUsername() {
        assertFalse(userService.isValidUser("abc"), "Expected false for username shorter than 4 characters");
    }

    @Test
    public void testIsValidUser_ValidUsername() {
        assertTrue(userService.isValidUser("abcd"), "Expected true for username with 4 or more characters");
    }

    @Test
    public void testIsValidUser_ExactBoundaryUsername() {
        assertTrue(userService.isValidUser("abcd"), "Expected true for username with exactly 4 characters");
    }

    @Test
    public void testIsValidUser_LongUsername() {
        assertTrue(userService.isValidUser("abcdefgh"), "Expected true for username longer than 4 characters");
    }
}
```