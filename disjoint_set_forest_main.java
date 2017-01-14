package artificial;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

class Main{
	
	public static void main (String[] args) {
		Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int m = in.nextInt();
            pair[] pairs = new pair[m];
            
            djNode[] nodeArray = new djNode[n];
            stackWithSize[] stackList = new stackWithSize[n];
            int[] stackSize = new int[n];
            for(int a2 = 0;a2<n;a2++){
                djNode temp = new djNode(a2);
                nodeArray[a2]= temp;
                Stack tstack = new Stack<djNode>();
                stackWithSize myStack = new stackWithSize(tstack,0);
            }
            for(int a1 = 0; a1 < m; a1++){
                int x = in.nextInt();
                int y = in.nextInt();
                pairs[a1] = new pair(x,y,nodeArray);
                stackList[x].pushElement(y);
                stackList[y].pushElement(x);  
            }
            
     
            long total = 0; // keep track of total friends after each iteration
            for(int i = 0; i<m;i++){
                pair correctPair = pairs[m-1];
                // Create a friendship between the two friends represented by correctpair
                // this is joining the sets they are in
                djNode nodeX = nodeArray[correctPair.x-1];
                djNode nodeY = nodeArray[correctPair.y-1];
                if(djNode.findSet(nodeX) != djNode.findSet(nodeY)){
                	djNode.union(nodeX,nodeY);
                }
                int size = Math.max(djNode.getSize(nodeX),djNode.getSize(nodeY));
                total+= size*(size-1);
                pairs[m-1] = new pair(-1,-1,nodeArray);
            }
            
            System.out.println(total);
        } // outer for
        
    }
}

