package b_4949;
import java.util.Stack;
import java.util.Scanner;

class b_4949 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		
		while(true) {
			String in=scan.nextLine();
			Stack<String> stk=new Stack<>();
			if(in.equals(".")) break;
			String[] str=in.split("");
			for(String s : str) {
				if(s.equals("(")||s.equals("[")) stk.push(s);
				else if(!stk.empty()&&s.equals(")")&&stk.peek().equals("(")) stk.pop();
				else if(!stk.empty()&&s.equals("]")&&stk.peek().equals("[")) stk.pop();
				else if(s.equals(")")||s.equals("]")) {
					stk.push(s); break;
				}
			}
			System.out.println(stk.empty()?"yes":"no");
		}
	}

}
