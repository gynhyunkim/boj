import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;
import java.io.IOException;

public class B_10430 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int[] arr = Arrays.stream(input.split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        System.out.println((arr[0] + arr[1]) % arr[2]);
        System.out.println(((arr[0] % arr[2]) + (arr[1] % arr[2])) % arr[2]);
        System.out.println((arr[0] * arr[1]) % arr[2]);
        System.out.println(((arr[0] % arr[2]) * (arr[1] % arr[2])) % arr[2]);
    }
}
