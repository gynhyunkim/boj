import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashMap;

public class B2026 {
	
	public static void main(String args[]) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int total = Integer.parseInt(br.readLine());
		int count = Integer.parseInt(br.readLine());
		HashMap hash = new HashMap();
		// int matrix[][] = new int[total][total];
		// boolean visited[] = new boolean[total];

		// for (int i = 0; i < total; i++) {
		// 	visited[i] = false;
		// 	for (int j = 0; j < total; j++) {
		// 		matrix[i][j] = 0;
		// 	}
		// }
		
		StringTokenizer st;
		for (int i = 0; i < count; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			if (hash.get(x) == null) {
				hash.put(x, new int[])
			}
		}


	}
}
