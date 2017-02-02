
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
       
        ArrayList<Integer> heapArray = new ArrayList<Integer>();
        int heapSize = 0;
        for(int a = 0;a<n;a++){
            int x = in.nextInt();
            int y = 0;
            if(x!=3) y = in.nextInt();

            if(x == 1){ // insert into heap
                heapInsert(heapArray,y);              
            }
            if(x == 2){
                deleteFromHeap(heapArray,y);
                maxHeapify(heapArray,0);
            }
            if(x==3){
               System.out.println(heapArray.get(0).toString());
            }
        }
    }
    public static void heapInsert(ArrayList<Integer> heapArray, int key){
        int heapSize = heapArray.size()+1;
        if(heapArray.size()==0){
            heapArray.add(key);
            return;
        }
        int temp = heapArray.get(0);
        heapArray.add(0,key);
        maxHeapify(heapArray,0);        
    }
    public static void maxHeapify(ArrayList<Integer> heapArray,int key){
        int l = (key+1)*2-1;
        int r = (key+1)*2;
        int smallest = -1;
        if(l < heapArray.size() && heapArray.get(l) < heapArray.get(key)) smallest = l;
        else smallest = key;
        if(r < heapArray.size() && heapArray.get(r) < heapArray.get(smallest)) smallest = r;
        if(smallest!=key){
            int temp =heapArray.get(key);
            heapArray.set(key, heapArray.get(smallest));
            heapArray.set(smallest, temp);
            maxHeapify(heapArray,smallest);
        }
    }
    public static void deleteFromHeap(ArrayList<Integer> heapArray,int key){
        int i = heapArray.indexOf(key);
        heapArray.remove(i);
    }
}
public class solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        ArrayList<Integer> heap = new ArrayList<Integer>();
        long answer = 0;
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        for(int a0=0;a0<n;a0++){
            heap.add(in.nextInt());
        }
        buildHeap(heap);
        // remove the smallest element from the heap, min-heapify, add it to the new smallest, minheapify
        while(true){
            int s = removeElement(heap);
            if(s<k && heap.size()==0){
                System.out.println("-1");
                return;
            }
            if(s>=k){
                System.out.println(answer);
                return;
            } 
            int temp = heap.get(0);
            heap.set(0,2*temp+s);
            answer++;
            minHeapify(heap,0);
        }       
    }    
    public static int removeElement(ArrayList<Integer> heap){
        int s = heap.get(0);
        heap.set(0,heap.get(heap.size()-1));
        heap.remove(heap.size()-1);
        minHeapify(heap,0);
        return s;
    }
    public static void buildHeap(ArrayList<Integer> heap){
        for(int i = heap.size()/2-1;i>=0;i--){
            
            minHeapify(heap,i);
        }
    }
    public static void minHeapify(ArrayList<Integer> heap, int key){
        // replace node with its smallest child until you can't anymore
        int smallest = key;
        int l = (key+1)*2-1;
        int r = (key+1)*2;
        if(l < heap.size() && heap.get(key) > heap.get(l)) smallest = l;
        if(r < heap.size() && heap.get(smallest) > heap.get(r)) smallest = r;
        // swap with smallest
        if(smallest!=key){
            int temp = heap.get(key);
            heap.set(key,heap.get(smallest));
            heap.set(smallest,temp);
            minHeapify(heap,smallest);
        }
    }
}
public class solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        int q = in.nextInt();
        int last_op = -1;
        for(int i = 0;i<q;i++){
            int x = in.nextInt();
            int y = 0;
            if(x==1) y= in.nextInt();
            if(x==1){
            	s1.push(y);
            	last_op = 1;
            }
            if(x==2){ // stack all elements to new stack (reversing order, then remove), then return to s1
            	if(!s2.isEmpty()){
            		s2.pop();
            	}
            	else{
            		while(!s1.isEmpty()){
                        s2.push(s1.pop());
                    }
                    s2.pop();
            	}          
            }
            if(x==3){
            	if(!s2.isEmpty()){
            		System.out.println(s2.peek());
            	}
            	else{
            		while(!s1.isEmpty()){
                        s2.push(s1.pop());
                    }
            		System.out.println(s2.peek());
            	}                       
            }
        }
    }
}