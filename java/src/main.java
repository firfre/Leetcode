public class main {

    public static void testTwoSum () {
        Solution aSolution = new Solution();
        int[] number = {2, 7, 11, 15};
        int[] result = aSolution.twoSum(number, 22);

        System.out.printf("Found index is %d and %d", result[0], result[1]);
    }

    public static void main(String[] args) {
        int problemID = 1;
        switch (problemID) {
            case 1: testTwoSum();
            break;
            default: throw new IllegalArgumentException("Undefined test cases!");
        }
    }
}

