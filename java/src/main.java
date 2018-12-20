public class main {
    public static void main(String[] args) {
        int problemID = 1;
        switch (problemID) {
            case 1: {
                TwoSum aSolution = new TwoSum();
                aSolution.test();
            }
            break;
            default: throw new IllegalArgumentException("Undefined test cases!");
        }
    }
}

