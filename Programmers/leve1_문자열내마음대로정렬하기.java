import java.util.Arrays;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer=new String[strings.length];
		int index=0;
		int stindex=0;
		for(int i=97;i<123;i++) {
			for(int j=0;j<strings.length;j++) {
				char c=strings[j].charAt(n);
				if(c==(char)i) answer[index++]=strings[j];
			}
			Arrays.sort(answer,stindex,index);
			stindex=index;
		}
		return answer;
    }
}