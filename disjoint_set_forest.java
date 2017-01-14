package artificial;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
class djNode {
	djNode parent;
	int size;
	int rank;
	int friend;

djNode(int friend){
	this.parent= this;
	this.size = 1;
	this.rank = 0;
	this.friend = friend;
}
public static int getSize(djNode x){
	return x.size;
}
public static int getFriend(djNode x){
	return x.friend;
}
public static djNode findSet(djNode x){
	if(x!=x.parent)x.parent = findSet(x.parent);
	return x.parent;
}
public static void link(djNode x, djNode y){
	if( x.rank > y.rank){
		y.parent = x;
		y.friend = x.friend;
		int temp = x.size;
		x.size+= y.size;
		y.size+=temp;
	}
	else{
		x.parent = y;
		x.friend=y.friend;
		if(x.rank == y.rank) y.rank++;
		int temp =  y.size;
		y.size+=x.size;
		x.size+=temp;
	}
}
public static void union(djNode x, djNode y){
	link(findSet(x),findSet(y));
}
}
class pair implements Comparable<pair> {
	int x;
	int y;
	djNode[] nodeArray;

pair(int x,int y, djNode[] narray){this.x =x;this.y=y;this.nodeArray = narray;}

public int compareTo(pair p2){
    
    if(this.x == -1 && p2.x == -1) return 0;
    else if(this.x == -1) return -1;
    else if(p2.x == -1) return 1;
	
	int x1;
	int x2;
	int y1;
	int y2;
	// Our comparison has to find the set each friend is in and the size of that set, takes the max of x,y pair set sizes
	djNode p1x = djNode.findSet(this.nodeArray[this.x-1]);
	x1 = djNode.getSize(p1x);
	djNode p1y = djNode.findSet(this.nodeArray[this.y-1]);
	y1 = djNode.getSize(p1y);	
	int total_p1 = 0;
	if(p1x!=p1y)total_p1 = x1+y1;
	
	
	
	djNode p2x = djNode.findSet(this.nodeArray[p2.x-1]);
	x2 = djNode.getSize(p2x);
	djNode p2y = djNode.findSet(this.nodeArray[p2.y-1]);
	y2 = djNode.getSize(p2y);	
	int total_p2 = 0;
	if(p2x!=p2y)total_p2 = x2+y2;
	
	
	if(total_p1 >total_p2) return 1;
	else if(total_p1 <total_p2) return -1;
	else return 0;
	
	
	
}
}
public class Solution {

    public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
	        int t = in.nextInt();
	        for(int a0 = 0; a0 < t; a0++){
	            int n = in.nextInt();
	            int m = in.nextInt();
	            pair[] pairs = new pair[m];
	            
                djNode[] nodeArray = new djNode[n];
                for(int a2 = 0;a2<n;a2++){
	                djNode temp = new djNode(a2);
	                nodeArray[a2]= temp;
	            }
	            for(int a1 = 0; a1 < m; a1++){
	                int x = in.nextInt();
	                int y = in.nextInt();
	                pairs[a1] = new pair(x,y,nodeArray);  
	            }
	            
	     
	            long total = 0; // keep track of total friends after each iteration
	            for(int i = 0; i<m;i++){
	                Arrays.sort(pairs);
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
