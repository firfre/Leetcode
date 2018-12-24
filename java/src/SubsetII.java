import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class SubsetII {
    static List<List<Integer>> solution(int[] numbers) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        result.add(new ArrayList<Integer>());
        Arrays.sort(numbers);
        int begin = 0;

        for(int i = 0; i < numbers.length; i++) {

            if(i == 0 || numbers[i] != numbers[i - 1]) {
                begin = 0;
            }
            int resultSize = result.size();
            for (int j = begin; j < resultSize ; j++) {
                List<Integer> aSubset = new ArrayList<Integer>(result.get(j));
                aSubset.add(numbers[i]);
                result.add(aSubset);
            }
            begin = resultSize;
        }

        return(result);
    }

    public static void test() {
        int[] numbers = {1, 1, 2};
        List<List<Integer>> result = solution(numbers);
        for(List<Integer> oneSubSet : result) {
            System.out.println(oneSubSet);
        }
    }
}
