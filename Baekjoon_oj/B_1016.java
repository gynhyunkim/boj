import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.lang.Math;

public class B_1016 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		long min = Long.parseLong(st.nextToken());
		long max = Long.parseLong(st.nextToken());
		long count = max - min + 1;
		boolean[] check = new boolean[(int)count];
		for (long i = 2; i * i <= max; i++) {
			long pow = i * i;
			long tmp = min / pow;
			if (min % pow != 0) {
				tmp++;
			}
			for (long j = tmp; j * pow <= max; j++) {
				int canSqrt = (int)(j * pow - min);
				if (!check[canSqrt]) {
					check[canSqrt] = true;
					count--;
				}
			}
		}
		System.out.println(count);
	}
}
