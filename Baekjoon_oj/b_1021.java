import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;

public class b_1021 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int size = Integer.parseInt(st.nextToken());
        int num = Integer.parseInt(st.nextToken());
        int[] targets = new int[num];
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < num; i++) {
            targets[i] = Integer.parseInt(st.nextToken());
        }

        LinkedList<Integer> deque = new LinkedList<>();
        for (int i = 0; i < size; i++) {
            deque.add(i + 1);
        }
		
		int idx, cnt = 0;
		for (int target : targets) {
			idx = deque.indexOf(target);
			size = deque.size();
			cnt += rotate(deque, (idx > size / 2), target);
			deque.poll();
		}
		System.out.println(cnt);
    }

    static int rotate(LinkedList<Integer> d, Boolean reverse, int target) {
		int cnt = 0;

		while (d.peek() != target) {
			if (reverse) {
				d.addFirst(d.pollLast());
			}
			else {
				d.addLast(d.poll());
			}
			cnt++;
		}
		return cnt;
    }
}
