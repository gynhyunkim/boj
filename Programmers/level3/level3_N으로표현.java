import java.util.*;

class Solution {
    
    static HashSet<Integer> calculate(List<Integer> A, List<Integer> B) {
        HashSet<Integer> result = new HashSet<>();
        
        for (int a : A) {
            for (int b : B) {
                result.add(a + b);
                result.add(a - b);
                result.add(a * b);
                if (b != 0) {
                    result.add(a / b);
                }
            }
        }
        return result;
    }
    
    public int solution(int N, int number) {
        int answer = 0;
        List<List<Integer>> dp = new ArrayList<>();
        
        for (int i = 0; i < 9; i++) {
            dp.add(new ArrayList<>());
        }
        for (int i = 1; i < 9; i++) {
            dp.get(i).add(Integer.parseInt(String.valueOf(N).repeat(i)));
            for (int j = 1; j < i; j++) {
                HashSet<Integer> result = calculate(dp.get(j), dp.get(i - j));
                for (int n : result) {
                    dp.get(i).add(n);
                }
            }
            if (dp.get(i).contains(number)) {
                return i;
            }
        }
        
        return -1;
    }
}

