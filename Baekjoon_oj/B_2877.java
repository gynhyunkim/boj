import java.util.Scanner;

public class B_2877 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt() + 1;
		StringBuilder sb = new StringBuilder();

		int num = 0;
		while (k != 0) {
			num = k % 2;
			sb.append(num);
			k /= 2;
		}
		int[] value = {4, 7};
		StringBuilder result = new StringBuilder();
		for (int i = sb.toString().length() - 2; i >= 0; i--) {
			result.append(value[sb.charAt(i) - '0']);
		}
		System.out.println(result.toString());
		sc.close();
	}
}
