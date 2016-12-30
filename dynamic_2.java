package artificial;
import java.io.*;
import java.util.*;
import java.text.*;
import java.lang.reflect.Array;
import java.math.*;
import java.util.regex.*;

public class solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    	try{
        	
    		BufferedReader br = 
    				new BufferedReader(new FileReader("laddusTest.txt"));
    		
    		
    		File file = new File("ladduAnswer.txt");
     
    		// if file doesnt exists, then create it
    		if (!file.exists()) {
    			file.createNewFile();
    		}
    		FileWriter fw = new FileWriter(file.getAbsoluteFile());
    		BufferedWriter bw = new BufferedWriter(fw);
        
	        int test_cases = Integer.parseInt(br.readLine().trim());
	        for(int i = 0;i<test_cases;i++){
	            int n = Integer.parseInt(br.readLine().trim());
	            String[] line = br.readLine().split(" ");
	            int[]a = new int [n];
	            
	            for(int j = 0;j<n;j++){a[j] = Integer.parseInt(line[j]);}
	            // array is populated
	            int running_sum = 0;
	            int[]b = new int [n];
	            for(int z = 0;z<n;z++){b[z] = Integer.MIN_VALUE;}
	            int answer = findMaxSub(a,running_sum,n-1,b);
	            
	            System.out.print(answer + " ");
	            int second_sum = 0;
	            int min = a[0];
	            for(int x = 0;x<n;x++){
	            	if(a[x] >=0){
	            		second_sum+= a[x];
	            	}
	            	if(a[x] > min)min = a[x];
	            }
	            if(second_sum==0)second_sum = min;
	            System.out.println(second_sum);
	        }
    	}
	        catch(IOException io){
	    		io.printStackTrace();
	    	}
    	
	        
    }
    public static int findMaxSub(int[] a, int sum,int end, int[] b){
        if (!(b[end] == Integer.MIN_VALUE)){ return b[end];}
        if(end == 0){
            if(a[0] >=0){
                b[0] = a[0]+sum;
                return b[0];
            }
            else{
            	b[0] = a[0]+sum;
                return b[0];
            } 
        }
        
        if(a[end] < 0 && -1*a[end] <= sum ){ 
        	int c[] = new int[end];
        	
            int temp =  sum;
            sum = sum + a[end];
            int value = findMaxSub(a,sum,end-1,b);
            b[end] = Math.max(sum,value);
            if(sum ==0 && value < 0){b[end] = value;}
        }
        else if(a[end] < 0 && -1*a[end] >sum){
        	int c[] = new int[end];
        	
        	sum = sum+a[end];
            int value = Math.max(sum,findMaxSub(a,0,end-1,b));
            b[end]= Math.max(sum,value); 
            if(sum ==0 && value < 0){b[end] = value;}
        }
        else{
        	int c[] = new int[end];
        
            sum = sum +a[end];
            int value = findMaxSub(a,sum,end-1,b);
            b[end] = Math.max(sum, value);
            if(sum ==0 && value < 0){b[end] = value;}
        }
        return b[end];                               
        
        
    }
}