import java.util.stream.*;
import java.util.Comparator;

class Solution {
    public String solution(String s) {
        String[] arr=s.split("");
        return Stream.of(arr).sorted(Comparator.reverseOrder()).collect(Collectors.joining());
    }
}