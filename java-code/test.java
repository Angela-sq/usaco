/* Use the slash-star style comments or the system won't see your
   identification information */
/*
ID: your_id_here
LANG: JAVA
TASK: test
*/
import java.io.*;
import java.util.*;

class test {
  public static void main (String [] args) throws IOException {
    // Use BufferedReader rather than RandomAccessFile; it's much faster
    BufferedReader fin = new BufferedReader(new FileReader("test.in"));
                                                  // input file name goes above
    PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("test.out")));
    // Use StringTokenizer vs. readLine/split -- lots faster
    StringTokenizer st = new StringTokenizer(fin.readLine());
						  // Get line, break into tokens
    int i1 = Integer.parseInt(st.nextToken());    // first integer
    int i2 = Integer.parseInt(st.nextToken());    // second integer
    fout.println(i1+i2);                           // output result
    fout.close();                                  // close the output file
  }
}
