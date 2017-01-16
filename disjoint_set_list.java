import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
class pair implements Comparable<pair>{
	int x;
	int y;
	int height;
	int size;
	

pair(int x, int y) {this.x =x;this.y=y;}
public int getX(){return this.x;}
public int getY(){return this.y;}
public void setSize(int x){this.size= x;}
public void setHeight(int x){this.height=x;}
@Override
public int compareTo(pair p2) {
	if(this.size > p2.size) return -1;
	else if(this.size < p2.size) return 1;
	else if(this.height > p2.height) return -1;
	else if(this.height < p2.height) return 1;
	else return 0;	
}
}
class djset {
	djNode head;
	djNode tail;
	int size;

djset(djNode x){
	this.head =x;
	this.tail=x;
	this.size =1;
}
public int getSize(){return this.size;}
}
class djNode {
	int friend;
	int height;
	djset set;
	djNode next;
/*this.head =x;
	this.tail=x;
	this.size =1;*/
djNode(int friend){
	this.height = 1;
	this.set = new djset(this);	
	this.friend=friend;
	this.next= null;
}
public int getHeight(){return this.height;}
public int getFriend(){return this.friend;}
public static djset findSet(djNode x){
	return x.set;
}
public static void link(djNode x, djNode y){
	if(x.set.getSize() <= y.set.getSize()){ // append x to back of y
		djNode head = x.set.head;
		djNode end_of_y = y.set.tail;
		end_of_y.next = head;
		end_of_y.next.height = end_of_y.height+1;
		y.set.size+=x.set.size;
		for(int i = 0; i<x.set.size;i++){			
			head.set = y.set;
			if(head.next==null){
				continue;
			}
			head.next.height=head.height+1;
			head= head.next;
		}
		y.set.tail = head;
		
	}
	else if (x.set.getSize()> y.set.getSize()){ // append y to back of x
		djNode head = y.set.head;
		djNode end_of_x = x.set.tail;
		end_of_x.next = head;
		end_of_x.next.height = end_of_x.height;
		for(int i = 0; i<y.set.size;i++){
			head.set = x.set;
			if(head.next == null)break;
			head.next.height=head.height+1;
			head= head.next;
		}
		x.set.tail = head;
		x.set.size += y.set.size;
	}
}
public static void union(djNode x, djNode y){
	link(x,y);
}
}
public class Solution {

    public static void main(String[] args) {
      
		Scanner in = new Scanner(System.in);	
        long t = in.nextLong();
        for(int a0 = 0; a0 < t; a0++){
        	
            long n = in.nextLong();
            long m = in.nextLong();
            pair[] pairs = new pair[(int) m+1];            
            djNode[] nodeArray = new djNode[(int) (n+1)];                
            for(int a2 = 1;a2<n+1;a2++){
                djNode temp = new djNode(a2);
                nodeArray[a2]= temp;         
            }
            for(int a1 = 1; a1 < m+1; a1++){ // this loop parses data and then creates our friendship if they are not already friends
            	
                int x = in.nextInt();
                int y = in.nextInt();
                djNode nodeX = nodeArray[x];
            	djNode nodeY = nodeArray[y];
            	pairs[a1] = new pair(x,y);
            	if(djNode.findSet(nodeX) == djNode.findSet(nodeY)){
            		continue;
            	}
            	else{
            		djNode.union(nodeX,nodeY);
            	}
            }
            for(int a3 = 1;a3<m+1;a3++){ // this loop gives pairs height and sizes to help sort (we want to choose the deepest
            	                        // element from the biggest tree first, then ignore all the other elements because
            	                       // we have built that tree and move on to the next tree
            	                      // this process gives us all our relevant links, then we do the rest of the links in arbitrary order
            	                     // which is just the same calculation x times, the link info doesn't even matter
            	int x = pairs[a3].getX();
            	int y = pairs[a3].getY();
            	djNode nodeX = nodeArray[x];
            	djNode nodeY = nodeArray[y];
            	// our set lists are all built
            	// when we look at a pair we need to choose the biggest set and biggest height
            	int size_x = nodeX.set.getSize();
            	int size_y = nodeY.set.getSize();
            	int size = Math.max(size_x,size_y);
            	int height;
            	if(size ==size_x)  height = nodeX.getHeight();
            	else height = nodeY.getHeight();
                pairs[a3].setSize(size);
                pairs[a3].setHeight(height);         
            }
            pairs[0]= new pair(-1,-1);
            Arrays.sort(pairs);
            
            
            // sorted by an element belongs to the largest set, if both belong we prioritize lowest rank because we are going
            // to start from root and link up to top for each set, once we get to head of set, we store that we are done with that
            // set in a hashmap and overlook any more pairs that are from that set because they don't increase length
            // and do those at the end
            HashSet<djset> setsFinished = new HashSet<djset>();
            LinkedList<Integer> setSizes = new LinkedList<Integer>();
            int non_adds = 0;
            int index = 0;
            for(int a4 = 0;a4<m;a4++){
            	
            	int x = pairs[a4].getX();
            	int y = pairs[a4].getY();
            	if(x==-1)continue;
            	djNode nodeX = nodeArray[x];
            	djNode nodeY = nodeArray[y];
            	djset currentSet = djNode.findSet(nodeX);
            	if(setsFinished.contains(currentSet)){
            		continue;
            	}
            	djNode leaf = nodeX;
            	if(nodeX.getHeight() > nodeY.getHeight()) leaf = nodeX.set.head;
            	else leaf = nodeY.set.head;
            	while(leaf.next!=null){ // after this loop, our biggest Set is filled, it takes 3 connections to make this set
            		pair newLink = new pair(leaf.getFriend(),leaf.next.getFriend());
            		pairs[index] = newLink;
            		index++;
            		leaf = leaf.next;
            	}
            	setSizes.add(currentSet.size);
            	setsFinished.add(currentSet);          
            }
            //we now have a list in descending order of the sizes of our friend groups
            // algorithm to computer total in loop below
            int total = 0;
            int pairs_used = 0;
            int prev_total = 0;
            while(!setSizes.isEmpty()){
            	int current_set_size = setSizes.removeFirst();
            	int rtotal = 0;
            	for(int i = 1;i<current_set_size;i++){
            		rtotal+= (i * (i+1));
            		prev_total =i * (i+1);
            		rtotal+=total;
            		pairs_used++;			
            	}
            	total+=rtotal;
            }
            total+= prev_total * (m-pairs_used);
            /*
            int total_pre_redundancy = total;
            // now we may have used less pairs than given, all the others are reduntant and we add them at end with no change to total
            // other than adding previous biggest totals
            for(int y = 0;y<(m-pairs_used);y++){
            	total+= total_pre_redundancy;	
            }
            */
          System.out.println(total);
        }
    }
}