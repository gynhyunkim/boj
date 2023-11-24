import java.util.Scanner;
public class B_1213 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String name = sc.nextLine();
		int[] alphaCount = new int[26];
		StringBuilder sb = new StringBuilder();
		StringBuilder left = new StringBuilder();
		StringBuilder right = new StringBuilder();
		char mid = '0';		

		for (Character c : name.toCharArray()) {
			alphaCount[c - 'A']++;
		}

		for (char i = 0; i < alphaCount.length; i++) {
			int cnt = alphaCount[i];
			char c = (char)(i + 'A');
			if (cnt % 2 > 0 && mid == '0') {
				mid = c;
			} else if (cnt % 2 > 0 && mid != '0') {
				sb = new StringBuilder("I'm Sorry Hansoo");
				break;
			}
			for (int j = 0; j < cnt / 2; j++) {
				left.append(c);
				right.insert(0, c);
			}
		}
		if (!sb.toString().equals("I'm Sorry Hansoo")) {
			sb.append(left);
			if (mid != '0') sb.append(mid);
			sb.append(right);
		}
		System.out.println(sb.toString());
		sc.close();
	}
	
}
