package artificial;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class solution {

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
		    int m = in.nextInt();
		    String s2 = in.next();
		    
			
			int x = 8;
			int i = 1;
			long answer = 0;
            boolean check = false;
			while(true){
				String s1 = Integer.toString(x*i);
                if(s1.length() > s2.length()) break;
				check = subsequenceCheck(s1,s2, s1.length(),m);
				if(check == true)answer++;
				i++;
                check = false;
			}
			System.out.println(answer % 1000000007);
    }
     public static boolean subsequenceCheck(String s1, String s2, int l1, int l2){
		  int j = 0;
		  for(int i = 0;i< l2 && j <l1;i++){
			  if(s1.charAt(j) == s2.charAt(i)) j++;
			  
		  }
		  return j==l1;
	  }
}