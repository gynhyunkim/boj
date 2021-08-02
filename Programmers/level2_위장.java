import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> count = new HashMap<>();
        
        for (String[] c : clothes) {
			count.put(c[1], count.getOrDefault(c[1], 0) + 1);
		}
        
        for (int i : count.values()) {
			answer *= (i + 1);
		}
        return (answer - 1);
    }
}