package artificial;



import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class solution {
  
     public static double solve(int[] arr, int N, int K) {
    	 double answer = 0;
    	 int val = 1- K;
    	 for(int i = 0;i<K;i++){
    		 answer+= val*arr[i];
    		 val+=2;
    	 
    	 }
    	 double global_answer = answer;
    	 int[] sum_arr = new int[N];
    	 sum_arr[0] = arr[0];
    	 for(int z = 1;z<N;z++){
    		 sum_arr[z]= sum_arr[z-1]+arr[z];
    	 }
    	 for(int i = K;i<N; i++){
    		 double temp = answer + (K-1)*arr[i]+(K-1)*arr[i-K]-2*(sum_arr[i-1] -sum_arr[i-K]);
    		 
    		 global_answer = Math.min(temp,global_answer);
    		 answer = temp;
    	 }
    	 
         return global_answer;   
         }
        
     
   

    public static void main(String[] args)  throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        int [] arr = new int[N];
        for(int i = 0; i < N; i++)
         arr[i] = Integer.parseInt(br.readLine());
        Arrays.sort(arr);
       
        double x = solve(arr,N,K);
        
        
        
        DecimalFormat decimalFormat=new DecimalFormat("#.#");
        System.out.println(decimalFormat.format(x));
    }
}