class Solution {
    public long solution(int a, int b) {
        long max=Math.max(a,b);
        long min=Math.min(a,b);
        return max*(max+1)/2-min*(min-1)/2;
    }
}