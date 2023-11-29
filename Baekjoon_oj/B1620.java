import java.util.HashMap;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1620 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        HashMap<String, Integer> indexByName = new HashMap<>();
        String[] indexByNum = new String[N + 1];
        for (int i = 1; i <= N; i++) {
            String name = br.readLine();
            indexByNum[i] = name;
            indexByName.put(name, i);
        }
        for (int i = 0; i < M; i++) {
            String input = br.readLine();
            try {
                int number = Integer.parseInt(input);
                System.out.println(indexByNum[number]);
            } catch (NumberFormatException ex) {
                System.out.println(indexByName.get(input));
            }
        }


    }

}
