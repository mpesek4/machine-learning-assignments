package artificial;

import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
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
            djNode[] nodeArray = new djNode[n+1];
            stackWithSize[] stackList = new stackWithSize[n+1];
            int[] stackSize = new int[n];
            for(int a2 = 1;a2<n+1;a2++){
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
            stackWithSize[] og_stackList = Arrays.copyOf(stackList,n+1);
            Arrays.sort(stackList);
            int[] orderArray= new int[n+1];
            // iterate over the sort list so we know what order the sets were turned into by examining their representative variable
            for(int x1 = 1; x1<n+1;x1++){
            	orderArray[x1] = stackList[x1].getRep();
            }
            // procedure works thus: remove all elements from the most filled stack, maintaining a "next stack" of these elements
            // to figure out order of stacks to deplete next, keep going until no elements left to remove
            // since elements xy are same as yx, we keep track ina  hashmap to see if element was already seen
            
            Queue<Integer> nextQueue = new LinkedList<Integer>();         
            HashMap<Integer,String> mymap = new HashMap<Integer,String>();
            int count = 0;
            for(int j = 1;j<n+1;j++){
            	if(count == m) break;
            	int current = og_stackList[orderArray[j]].getRep();
            	while(stackList[j].checkEmpty() == false){
            		if(count == m) break;
            		String t1 = "";
            		pair npair = new pair(-1,-1);
            		int xb =current;
            		int yb= stackList[j].popElement();
            		if(xb > yb) {
            			t1 = t1+Integer.toString(yb)+Integer.toString(xb);
            			npair = new pair(yb,xb);
            		}
                	if(xb < yb){
                		t1 = t1+Integer.toString(xb)+Integer.toString(yb);
                		npair = new pair(xb,yb);
                	}
                	int code = t1.hashCode();
                	if(mymap.get(code) == null){
                		mymap.put(code,t1);
                		pairs[count] = npair;
                		count++;
                		nextQueue.add(yb);               		
                		if(count==m)break;
                		
                	}           	          		
            	}
            	while(!(nextQueue.peek() == null)){
            		if(count==m)break;
            		int curr = nextQueue.remove();
                	String tmp = "";
                	pair mpair = new pair(-1,-1);
                	int xc = og_stackList[curr].getRep(); // x value of our pair is just the rep, y value is the stack value
                	int yc = og_stackList[curr].popElement();
                	if(yc == -1) continue;
                	if(xc > yc) {
                		tmp = tmp+Integer.toString(yc)+Integer.toString(xc);
                		mpair = new pair(yc,xc);
                	}
                	if(xc < yc) {
                		tmp = tmp+Integer.toString(xc)+Integer.toString(yc);
                		mpair = new pair(xc,yc);
                	}
                	int code = tmp.hashCode();
                	if(mymap.get(code) == null){
                		mymap.put(code,tmp);
                		pairs[count] = mpair;
                		count++;
                		nextQueue.add(yc);
                		if(count==m)break;
                		
                	}           	
            	}
            }
            long total = 0; // keep track of total friends after each iteration
            djNode prevX = new djNode(-1);
            djNode prevY = new djNode(-1);
            long prev_total = 0;
            for(int i = 0; i<m;i++){
                pair correctPair = pairs[i];
                // Create a friendship between the two friends represented by correctpair
                // this is joining the sets they are in
                djNode nodeX = nodeArray[correctPair.x];
                djNode nodeY = nodeArray[correctPair.y];
                boolean union_done = false;
                if(djNode.findSet(nodeX) != djNode.findSet(nodeY)){
                	djNode.union(nodeX,nodeY);
                	union_done = true;
                }
                long size = Math.max(djNode.getSize(nodeX),djNode.getSize(nodeY));
                long round_total = size*(size-1);
                boolean check = djNode.findSet(nodeX) == djNode.findSet(prevX) || djNode.findSet(nodeY) == djNode.findSet(prevX);
                if(check){
                	// we are adding to same set as previous iteration, we just add to total
                	long set_size = djNode.getSize(djNode.findSet(prevX));
                	long size_pre = (set_size-1)* (set_size-2);
                	long size_post = set_size * (set_size-1);
                	// if however both new elements were already in that set, size_pre is just set_size
                	if(check && !union_done){
                		total+=prev_total;
                	}
                	else{ 
                		total+= prev_total+size_post-size_pre;
                		round_total = prev_total+size_post-size_pre;
                	}
                }
                else{
                	total+= prev_total+round_total;
                	round_total = prev_total+round_total;
                }
                prevX = nodeX;
                prevY = nodeY;
                prev_total = round_total;
                              
            }          
            System.out.println(total);
        } // outer for
        
    }
}

