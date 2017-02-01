import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
class Node {
    int depth;
    int data;
    Node left;
    Node right;

public static void inOrder(Node root) {
    
    if(root.left!=null)inOrder(root.left);
    System.out.print(root.data + " ");
    if(root.right!=null)inOrder(root.right);
}
}
public class solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        LinkedList<Node> ith_Nodes = new LinkedList<Node>();
        Node start = new Node();
        for(int c =1;c<=n;c++){
        	Node temp = new Node();
        	temp.data = c;
        	ith_Nodes.add(temp);
        }
        for (int a=1;a<=n;a++){
        	Node temp = ith_Nodes.get(a-1);
            int x = in.nextInt();
            int y = in.nextInt();
            if(x!=-1){
                Node leftChild = ith_Nodes.get(x-1);
                leftChild.data =x;
                temp.left = leftChild;
            }
            if(y!=-1){
                Node rightChild = ith_Nodes.get(y-1);
                rightChild.data =y;
                temp.right = rightChild;
            }
        } // Tree is constructed
        // Go down to the required depths
        start = ith_Nodes.get(0);
        start.depth = 1;
        int numk = in.nextInt();
        for(int a1=0;a1<numk;a1++){
            int k = in.nextInt();
            performSwap(k,start);
            Node.inOrder(start);
            System.out.println();
        }   
}
    public static void performSwap(int k,Node start){
        LinkedList<Node> q = new LinkedList<Node>();
        q.add(start);
        while(!q.isEmpty()){
            Node head = q.remove();
            
            if(head.left!=null){
                head.left.depth = head.depth+1;
                q.add(head.left);
            }
            if(head.right!=null){
                head.right.depth = head.depth+1;
                q.add(head.right);
            }
            if(head.depth %k == 0 && head.depth>0){
                Node temp = head.left;
                head.left = head.right;
                head.right = temp;
            }
        }
    }
}