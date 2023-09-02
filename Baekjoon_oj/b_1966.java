import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Collections;

class b_1966 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Queue<Integer> queue;

        int test = Integer.parseInt(br.readLine()); // 읽은 문자열을 정수로 변환해서 대입
        int doc, pos;
        while (test-- > 0) {
            queue = new LinkedList<>();
            st = new StringTokenizer(br.readLine());
            doc = Integer.parseInt(st.nextToken());
            pos = Integer.parseInt(st.nextToken()); 

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < doc; i++) {
                queue.offer(Integer.parseInt(st.nextToken()));
            }
            while (pos != -1) {
                int max = Collections.max(queue);
                if (max != queue.peek()) {
                    queue.offer(queue.poll());
                    pos = pos != 0 ? pos - 1 : queue.size() - 1;
                }
                else {
                    queue.poll();
                    if (pos == 0) {
                        System.out.println(doc - queue.size());
                        pos = -1;
                    }
                    else {
                        pos--;
                    }
                }
                
            }
        }
    }
}
