import java.util.*;

class Solution {
    static Queue<Integer> q = new LinkedList<>();
    
    public static void BFS(int n, int[][] computers) {
        while (!q.isEmpty()) {
            int curr = q.poll();
            for (int i = 0; i < n; i++) {
                if (computers[curr][i] == 1 && computers[i][i] == 1) {
                    q.offer(i);
                    computers[i][i] = 0;
                }
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        for (int i = 0; i < n; i++) {
            if (computers[i][i] == 1) {
                q.offer(i);
                computers[i][i] = 0;
                BFS(n, computers);
                answer++;
            }
        }
        return answer;
    }
}

