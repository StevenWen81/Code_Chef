import java.util.*;
import java.lang.*;
import java.io.*;

class Chess_Match
{
	public static void main (String[] args) throws java.lang.Exception
	{
	  Scanner Sc=new Scanner(System.in);
		int t=Sc.nextInt();
		while(t-->0)
		{
			int n,a,b;
			n=Sc.nextInt();
			a=Sc.nextInt();
			b=Sc.nextInt();
			System.out.println(2*(180+n)-a-b);
		}
	}
}