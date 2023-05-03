import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int N = nums.length / 2;
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (!map.containsKey(num)) {
                map.put(num, 0);
            }
            map.put(num, map.get(num) + 1);
        }
        return N <= map.size() ? N : map.size();
    }
}

