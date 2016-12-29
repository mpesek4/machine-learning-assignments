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
        Scanner in = new Scanner(System.in);
        for(int i = 0;i<in.nextInt();i++){
            int n = in.nextInt();
            int[] a = new int[n];
            for(int j = 0;j<n;j++){a[j] = in.nextInt();}
            // array is populated
            int running_sum = 0;
            int[]b = new int [n];
            for(int z = 0;z<n;z++){b[z] = Integer.MIN_VALUE;}
            int answer = findMaxSub(a,running_sum,n-1,b);
            System.out.println(answer);
            
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
                return 0;
            } 
        }
        
        if(a[end] < 0 && -1*a[end] <= sum ){ 
        	int c[] = new int[end];
        	c = Arrays.copyOfRange(a,0,end);
            int temp =  sum;
            sum = sum + a[end];
            sum+= Math.max(temp,findMaxSub(c,sum,end-1,b));
            b[end] = sum;
        }
        else if(a[end] < 0 && -1*a[end] >sum){
        	int c[] = new int[end];
        	c = Arrays.copyOfRange(a,0,end);
            sum = Math.max(sum,findMaxSub(c,0,end-1,b));
            b[end]= sum;        
        }
        else{
        	int c[] = new int[end];
        	c = Arrays.copyOfRange(a,0,end);
            sum = sum +a[end];
            int value = findMaxSub(a,sum,end-1,b);
            b[end] = Math.max(sum, value);
        }
        return b[end];                               
        
        
    }
}