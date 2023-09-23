import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Exception;

public class 9655 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamReader(System.out));

		int N = Integer.parseInt(br.readLine());
		
		bw.write((N % 2 == 1) ? "SK" : "CY");
		bw.flush();
		br.close();
		bw.close();
	}
}