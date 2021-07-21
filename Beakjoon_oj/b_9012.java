import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class b_9012 {
    static Stack<String> s1;
    static Stack<String> s2;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cases = Integer.parseInt(br.readLine());
        String str;

        while (cases-- > 0) {    
            s1 = new Stack<>();
            str = br.readLine();
            for (int i = 0; i < str.length(); i++) {
                s1.add(str.substring(i, i + 1));
            }
            System.out.println(isVPS());
        }

    }

    static String isVPS() {
        String cur;
        s2 = new Stack<>();
        while (!s1.isEmpty()) {
            cur = s1.pop();
            if (cur.equals(")")) {
                s2.add(cur);
            }
            else if (cur.equals("(") && !s2.isEmpty()) {
                s2.pop();
            }
            else {
                return "NO";
            }
        }
        if (s2.isEmpty())
            return "YES";
        return "NO";
    }
}
