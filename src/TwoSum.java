import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    private static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("solution not found!");
    }

    public static void main(String[] args) {
        int[] number = {2, 7, 11, 15};
        int[] result = twoSum(number, 22);

        System.out.printf("Found index is %d and %d", result[0], result[1]);
    }
}
