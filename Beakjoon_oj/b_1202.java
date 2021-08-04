import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Arrays;

public class b_1202 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		ArrayList<Gem> q = new ArrayList<>();
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			q.add(new Gem(m, v));
		}
		Collections.sort(q, (o1, o2) -> o1.m - o2.m);
		int[] bags = new int[k];
		for (int i = 0; i < k; i++) {
			bags[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(bags);
		int cnt = 0;
		int j = 0;
		PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

		for (int bag : bags) {
			while (j < n && q.get(j).m <= bag) {
				pq.offer(q.get(j).v);
				j++;
			}
			cnt += pq.isEmpty() ? 0 : pq.poll();
		}

		System.out.println(cnt);
	}


	static class Gem {
		int m;
		int v;

		public Gem(int m, int v) {
			this.m = m;
			this.v = v;
		}		
	}
}
