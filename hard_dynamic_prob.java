package artificial;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class solution {
  
     public static int solve(int[] arr, int N, int K) {
         int max_range = Integer.MAX_VALUE;
         int Ki = 0;
         int first_index = 0;
         for(int i = 0;i< arr.length;i++){
             if(i+K-1 > arr.length - 1)continue;
             int range_check = arr[i+K-1]-arr[i];
             if(range_check < max_range){
                 max_range = range_check;
                 first_index = i;
             }
         }
         return first_index;    
             
         }
        
     
    public static int calc_unfairness(int[] arr, int first_index, int K){
        int unfairness = 0;
        for(int i = first_index;i <=first_index+K-1;i++){
            for(int j = i+1;j <=first_index+K-1;j++){
                if(i==j || i > j)continue;
                
                unfairness+= arr[j]-arr[i];
            }
        }
        return unfairness;
    }

    public static void main(String[] args)  throws Exception {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         int N = Integer.parseInt(br.readLine());
         int K = Integer.parseInt(br.readLine());
         int [] arr = new int[N];
         for(int i = 0; i < N; i++)
          arr[i] = Integer.parseInt(br.readLine());
         Arrays.sort(arr);
         int first_index = solve(arr, N, K);
         System.out.println(calc_unfairness(arr,first_index,K));
    }
}