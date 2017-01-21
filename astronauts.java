package artificial;


import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
class countryNode {
	LinkedList<countryNode> adjList = new LinkedList<countryNode>();
	int country;
	String color;
	int size;
	countryNode(int x){this.country = x;this.color ="white";this.size=1;}
	public void addElement(countryNode x){this.adjList.add(x);}
}
public class Main{
	
	 public static void main(String[] args) {
	        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
		 Scanner in = new Scanner(System.in);
	        String[] line1 = in.nextLine().split(" ");
	        int n = Integer.parseInt(line1[0]);
	        int i = Integer.parseInt(line1[1]);
	        LinkedList<countryNode> allAstronauts = new LinkedList<countryNode>();
	        for(int a= 0;a<n;a++){
	        	// create a node class that will be used for graphs
	        	countryNode astronaut = new countryNode(a);
	        	allAstronauts.add(astronaut);	        	
	        }
	        for(int j = 0;j<i;j++){
	        	String [] nextLine = in.nextLine().split(" ");
	        	int a = Integer.parseInt(nextLine[0]);
	        	int b = Integer.parseInt(nextLine[1]);
	        	allAstronauts.get(a).addElement(allAstronauts.get(b));
	        	allAstronauts.get(b).addElement(allAstronauts.get(a));
	        }
	        HashSet<countryNode> populated = new HashSet<countryNode>();
	        //Begin a DFS on node to populate graphs, every node visited is added to populated
	        
	        ListIterator<countryNode> li2 = allAstronauts.listIterator();
	        // now we have some number of connect components that represent our countries
	        // we start at any node and do a DFS, any node visited is added to populated hashmap so we only visit each node once
	        // after a node is done populating a graph, we store the size
	        LinkedList<Integer> sizes = new LinkedList<Integer>();
	        int runningSize = 0;
	        long singles = 0;
	        while(li2.hasNext()){
	        	countryNode current = li2.next();
	        	if(populated.contains(current))continue;
	        	if(current.color.equals("white")){
	        		DFSV(allAstronauts,current,populated);
	        	}
	        	int temp = runningSize;
	        	runningSize = 0;
	        	runningSize+= populated.size();
	        	if(runningSize-temp == 1)singles++;
	        	else sizes.add(runningSize-temp);
	        }
	        long answer = 0;
	        long prefix = 0;
	        Object[] sizeArray = sizes.toArray();
	        for(int a5=0;a5<sizeArray.length;a5++){
	        	prefix+= ((Integer) sizeArray[a5]).longValue();
	        }
	        for(int a3 = 0;a3<sizeArray.length;a3++){
	        	for(int a4=a3+1;a4<sizeArray.length;a4++){
	        		answer+= ((Integer) sizeArray[a3]).longValue() * ((Integer) sizeArray[a4]).longValue();
	        	}
	        }
	        answer+= prefix*(singles) + ((singles-1)*(singles)) / 2;
	        System.out.println(answer);
	}
	 public static void DFSV(LinkedList<countryNode> allAstronauts, countryNode current,HashSet<countryNode> populated){
		 current.color = "grey";
		 populated.add(current);
		 for(int i = 0;i< current.adjList.size();i++){
			 ListIterator<countryNode> li = current.adjList.listIterator();
			 while(li.hasNext()){
				 countryNode next = li.next(); 
				 if(next==current){
					 continue;
				 }
				 if(next.color.equals("white")) DFSV(allAstronauts,next,populated);
				 
			 }//while
			 /*
			 while(!q.isEmpty()){// we know these are in currents adjacency list, so current must be in their adjList
					// this guarantees we have both directions covered so we can do full dfs from any node
					// later to find our countries
				 countryNode temp = q.poll();
				 li.add(current); */
			 }
		current.color = "black"; 
	 }
}

	