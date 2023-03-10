import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B3085 {

	static int size, max = 0;
	static String[] candy;

	public static void findMax(int i, int j)
	{
		int max_i = 1, max_j = 1; 
		for (int idx = 1; idx < size; idx++) {
			if (candy[i].charAt(idx - 1) != candy[i].charAt(idx))
				max_i = 0;
			else
				max_i++;
			if (candy[idx - 1].charAt(j) != candy[idx].charAt(j))
				max_j = 0;
			else
				max_j++;
		}
		if (max_i >= max_j)
			max = max < max_i ? max_i : max;
		else
			max = max < max_j ? max_j : max;
	} 
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		size = Integer.parseInt(br.readLine());
		
		candy = new String[size];
		for (int i = 0; i < size; i++)
			candy[i] = br.readLine();
		
		for (int i = 0; i < size; i++)
			for (int j = 0; j < size; j++)
				findMax(i , j);
		System.out.print(max);
	}
}