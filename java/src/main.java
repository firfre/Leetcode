public class main {
    public static void main(String[] args) {
        int problemID = 90;
        switch (problemID) {
            case 1: {
                TwoSum aSolution = new TwoSum();
                aSolution.test();
            }
            break;
            case 90: {
                SubsetII aSolution = new SubsetII();
                aSolution.test();
            }
            break;
            default: throw new IllegalArgumentException("Undefined test cases!");
        }
    }
}

