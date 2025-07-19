public class UserService {
    public boolean isValidUser(String username) {
        return username != null && username.length() > 3;
    }
}
