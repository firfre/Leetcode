import java.util.HashMap;
import java.util.Map;

// example solution from Leetcode
class TwoSum {
    static int[] solution(int[] nums, int target) {
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

    public static void test() {
        int[] number = {2, 7, 11, 15};
        int[] result = solution(number, 22);

        System.out.printf("Found index is %d and %d", result[0], result[1]);
    }
}