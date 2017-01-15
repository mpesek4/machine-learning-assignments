package artificial;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
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
            LinkedList<pair> savedForLast = new LinkedList<pair>();
            HashMap<Integer,String> mymap = new HashMap<Integer,String>();
            int count = 0;
            LinkedList<HashSet<Integer>> sets = new LinkedList<HashSet<Integer>>();
            
           // keep track of total friends after each iteration
            djNode prevX = new djNode(-1);
            djNode prevY = new djNode(-1);
            long[] prev_total = new long[1];
            long[] total = new long[1];
            djNode[] prev_x_y = new djNode[2];
            prev_x_y[0] = prevX;
            prev_x_y[1] = prevY;
            int non_adds = 0;
            for(int j = 1;j<n+1;j++){
            	HashSet<Integer> elements_added = new HashSet<Integer>();
            	if(count == m) break;
            	int current = og_stackList[orderArray[j]].getRep();
            	elements_added.add(current);
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
                	boolean found = false;
                	if(mymap.get(code) == null){
                		mymap.put(code,t1);
                	//	pairs[count] = npair; instead of saving pairs for later, update total as we go because we do it in correct order anyway
                		djNode nodeX = nodeArray[xb];
                		djNode nodeY = nodeArray[yb];
                		if(djNode.findSet(nodeX) == djNode.findSet(nodeY)){
                			// this is the case where we don't increase our friend sets, we save these for last
                			count++;
                			non_adds++;
                		}
                		// public static void updateTotal(djNode[] prev_x_y,djNode nodeX,djNode nodeY, long[] prev_total, long[] total){
                		else{
                			updateTotal(prev_x_y,nodeX,nodeY,prev_total,total);
                    		count++;
                    		nextQueue.add(yb);  
                    		elements_added.add(yb);
                		}              		
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
                		//pairs[count] = mpair;
                		djNode nodeX = nodeArray[xc];
                		djNode nodeY = nodeArray[yc];
                		if(djNode.findSet(nodeX) == djNode.findSet(nodeY)){
                			// this is the case where we don't increase our friend sets, we save these for last
                			count++;
                			non_adds++;
                		}
                		// public static void updateTotal(djNode[] prev_x_y,djNode nodeX,djNode nodeY, long[] prev_total, long[] total){
                		else{
                			updateTotal(prev_x_y,nodeX,nodeY,prev_total,total);
                    		count++;
                    		nextQueue.add(yc);                  		
                		}            	              		
                	}                	
            	}
            } //outer for
            
            for (int s = 0;s < non_adds;s++){
            	total[0]+= prev_total[0];       	
            }
            System.out.println(total[0]);
        } // outer for
        
    }
	public static void updateTotal(djNode[] prev_x_y,djNode nodeX,djNode nodeY, long[] prev_total, long[] total){
		boolean union_done = false;
        if(djNode.findSet(nodeX) != djNode.findSet(nodeY)){
        	djNode.union(nodeX,nodeY);
        	union_done = true;
        }
        long size = Math.max(djNode.getSize(nodeX),djNode.getSize(nodeY));
        long round_total = size*(size-1);
        boolean check = djNode.findSet(nodeX) == djNode.findSet(prev_x_y[0]) || djNode.findSet(nodeY) == djNode.findSet(prev_x_y[0]);
        if(check){
        	// we are adding to same set as previous iteration, we just add to total
        	long set_size = djNode.getSize(djNode.findSet(prev_x_y[0]));
        	long size_pre = (set_size-1)* (set_size-2);
        	long size_post = set_size * (set_size-1);
        	// if however both new elements were already in that set, size_pre is just set_size
        	if(check && !union_done){
        		total[0]+=prev_total[0];
        	}
        	else{ 
        		total[0]+= prev_total[0]+size_post-size_pre;
        		round_total = prev_total[0]+size_post-size_pre;
        	}
        }
        else{
        	total[0]+= prev_total[0]+round_total;
        	round_total = prev_total[0]+round_total;
        }
        prev_x_y[0] = nodeX;
        prev_x_y[1] = nodeY;
        prev_total[0] = round_total;
	}
}

