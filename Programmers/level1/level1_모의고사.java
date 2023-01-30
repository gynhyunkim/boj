class Solution {
    public int[] solution(int[] answers) {
        int[] cnt={0,0,0};
        int[] fir={1,2,3,4,5};
        int[] sec={2,1,2,3,2,4,2,5};
        int[] thr={3,3,1,1,2,2,4,4,5,5};
        for(int i=0;i<answers.length;i++){           
            if(answers[i]==fir[i%5]) cnt[0]++;
            if(answers[i]==sec[i%8]) cnt[1]++;
            if(answers[i]==thr[i%10]) cnt[2]++;
        }
        int leng=1;
		int max=cnt[0];
		for(int i=1;i<3;i++) {
			if(max<cnt[i]) {
				if(leng>1) leng--;
                max=cnt[i];
			}
			else if(max==cnt[i]) leng++;
		}
		int[] answer=new int[leng];
		for(int i=0,j=0;i<3;i++) {
			if(cnt[i]==max) { answer[j]=i+1; j++;}
		}
        return answer;
    }
}