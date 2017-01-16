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
class pair {
	int x;
	int y;

pair(int x, int y) {this.x =x;this.y=y;}
}
class stackWithSize implements Comparable<stackWithSize> {
    Stack<Integer> s;
	int n;
	int rep;
	
	
stackWithSize(Stack<Integer> s, int n,int rep){this.s = s;this.n =n;this.rep=rep;}

public void incrementStack(){this.n++;}
public int getRep(){return this.rep;}
public boolean checkEmpty(){ return this.s.empty();}
public int  popElement(){
	if(this.s.empty()) return -1;
	int y = this.s.pop();
	return y;
}
public int compareTo(stackWithSize s2){
	if(this.n > s2.n) return -1;
	else if(this.n < s2.n) return 1;
	else return 0;
}

public void pushElement(int y) {
	this.s.push(y);
	this.n++;
	
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
            stackWithSize[] stackList = new stackWithSize[n];
            int[] stackSize = new int[n];
            for(int a2 = 0;a2<n;a2++){
                djNode temp = new djNode(a2);
                nodeArray[a2]= temp;
                Stack<Integer> tstack = new Stack<Integer>();
                stackWithSize myStack = new stackWithSize(tstack,0,a2);
                stackList[a2] = myStack;
            }
            for(int a1 = 0; a1 < m; a1++){
                int x = in.nextInt();
                int y = in.nextInt();
                pairs[a1] = new pair(x,y);
                stackList[x].pushElement(y);
                stackList[y].pushElement(x);  
            }
            Arrays.sort(stackList);
            int[] orderArray= new int[n];
            // iterate over the sort list so we know what order the sets were turned into by examining their representative variable
            for(int x1 = 0; x1<n;x1++){
            	orderArray[x1] = stackList[x1].getRep();
            }
            // procedure works thus: remove all elements from the most filled stack, maintaining a "next stack" of these elements
            // to figure out order of stacks to deplete next, keep going until no elements left to remove
            // since elements xy are same as yx, we keep track ina  hashmap to see if element was already seen
            
            Queue<Integer> nextQueue = new LinkedList<Integer>();         
            HashMap<Integer,pair> mymap = new HashMap<Integer,pair>();
            int count = 0;
            for(int j = 0;j<n;j++){
            	if(count == n-1) break;
            	int current = stackList[j].getRep();
            	while(stackList[j].checkEmpty() == false){
            		if(count == n) break;
            		pair t1 = new pair(-1,-1);
            		int xb =current;
            		int yb= stackList[j].popElement();
            		if(xb > yb)  t1 = new pair(yb,xb);
                	if(xb < yb)  t1 = new pair(xb,yb);
                	int code = t1.hashCode();
                	if(mymap.get(code) == null){
                		mymap.put(code,t1);
                		pairs[count] = t1;
                		count++;
                		if(count==n)break;
                		nextQueue.add(yb);
                	}           	          		
            	}
            	while(!(nextQueue.poll() == null)){
            		if(count==n-1)break;
            		int curr = nextQueue.remove();
                	pair tmp = new pair(-1,-1);
                	int xc = stackList[curr].getRep(); // x value of our pair is just the rep, y value is the stack value
                	int yc = stackList[curr].popElement();
                	if(yc == -1) continue;
                	if(xc > yc)  tmp = new pair(yc,xc);
                	if(xc < yc)  tmp = new pair(xc,yc);
                	int code = tmp.hashCode();
                	if(mymap.get(code) == null){
                		mymap.put(code,tmp);
                		pairs[count] = tmp;
                		count++;
                		if(count==n-1)break;
                		nextQueue.add(yc);
                	}           	
            	}
            }
            long total = 0; // keep track of total friends after each iteration
            for(int i = 0; i<m;i++){
                pair correctPair = pairs[i];
                // Create a friendship between the two friends represented by correctpair
                // this is joining the sets they are in
                djNode nodeX = nodeArray[correctPair.x-1];
                djNode nodeY = nodeArray[correctPair.y-1];
                if(djNode.findSet(nodeX) != djNode.findSet(nodeY)){
                	djNode.union(nodeX,nodeY);
                }
                int size = Math.max(djNode.getSize(nodeX),djNode.getSize(nodeY));
                total+= size*(size-1);                
            }          
            System.out.println(total);
        } // outer for
        
    }
}
