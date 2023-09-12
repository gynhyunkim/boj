// 최대 힙
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class b_11279 {
	
	static int heap[];
	static int index;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
		int cnt = Integer.parseInt(br.readLine());
		heap = new int[cnt + 1];
		index = 0;

		while (cnt-- > 0) {
			int x = Integer.parseInt(br.readLine());
			
			if (x == 0) {
				sb.append(poll() + "\n");
			}
			else {
				insert(x);
			}
		}
		System.out.println(sb);
	}

	static void swap(int a, int b) {
		int tmp = heap[a];
		heap[a] = heap[b];
		heap[b] = tmp;
	}

	static void insert(int val) {
		heap[++index] = val;
		
		int i = index;
		while (i > 1 && heap[i / 2] < heap[i]){
			swap(i, i / 2);
			i /= 2;
		}
	}

	static int poll() {
		if (index == 0) {
			return (0);
		}
		int deletedItem = heap[1];
		heap[1] = heap[index--];
		for (int i = 1; i * 2 <= index;) {
			if (heap[i] > heap[i * 2] && heap[i] > heap[i * 2 + 1]){
				break;
			}
			else if(heap[i * 2] > heap[i * 2 + 1]) {
				swap(i, i * 2);
				i = i * 2;
			} else {
				swap(i, i * 2 + 1);
				i = i * 2 + 1;
			}
		}
		return (deletedItem);
	}
}
