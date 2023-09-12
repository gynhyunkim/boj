package b_10828;
import java.util.Scanner;

public class b_10828 {
	static class Node{
		int item;
		Node nextNode;
		public Node(int newItem,Node newNode){
			item=newItem;
			nextNode=newNode;
		}
		public Node getNext() { return nextNode; }
		public int getItem() { return item; }
	}
	static class myStack{
		Node root=null;
		int size=0;
		
		public void push(int x) {
			root=new Node(x,root);
			size++;
		}
		public void pop() {
			top();
			if(root!=null) {
				root=root.getNext();
				size--;
			}
		}
		public void getSize() { System.out.println(size); }
		public void empty() { System.out.println(size==0 ? 1 : 0);}
		public void top() {
			System.out.println(size==0?-1:root.getItem());
		}
	}
	

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int size=scan.nextInt();
		myStack s1=new myStack();
	
		scan.nextLine();
		for(int i=0;i<size;i++) {
			String str1=scan.nextLine();
			String[] arr=str1.split(" ");
			if(arr.length==1) {
				if(arr[0].equals("top")) s1.top();
				else if(arr[0].equals("size")) s1.getSize();
				else if(arr[0].equals("pop")) s1.pop();
				else s1.empty();
			}
			else {s1.push(Integer.parseInt(arr[1]));}
		}
	}
	
}
