package artificial;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.math.BigInteger;


	public class solution {

	    public static void main(String[] args) {
	        Scanner in = new Scanner(System.in);
	        int term1 = in.nextInt();
	        int term2 = in.nextInt();
	        int n =  in.nextInt();
	        String [] c = new String [22];
	        for(int i = 2;i <22;i++){ c[i] = "-1";}
	        	
	        c[1] = Integer.toString(term1);
	        c[2] = Integer.toString(term2);
	            
	    		
	        String answer = fib_n(n,c);
	    	//for(int i = 0;i<22;i++){System.out.println(c[i]);}
	    	System.out.println(c[n]);
		    }
	    public static String fib_n (int n,String [] c){
	    	if (n==0){ return c[0];}
	    	else if (n==1) { return c[1];}
	    	else{
	    		if (!c[n].equals("-1")){ return c[n];}
	    		else{
	    			BigInteger nmin2 = new BigInteger(fib_n(n-2,c));
	    			BigInteger nmin1 = new BigInteger(fib_n(n-1,c));
	    			BigInteger term = nmin2.add(nmin1.multiply(nmin1));
	    			c[n] = term.toString();
	    			return term.toString();
	    		}
	    	}
	    	
	    	
	    	
	    }
	}
