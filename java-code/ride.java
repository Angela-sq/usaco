/*
ID: angela.14
LANG: JAVA
TASK: ride
*/
import java.io.*;

class ride{
    public static void main (String [] args) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("ride.in"));
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("ride.out")));
        String line1 = fin.readLine();
        String line2 = fin.readLine();

        String result = null;
        if (convertInt(line1) % 47 == convertInt(line2) % 47) {
            result = "GO";
        }
        else {
            result = "STAY";
        }

        fout.println(result);
        fout.close();   

    }

    public static int convertInt (String line) {
        int product = 1;
        int charLen = line.length();
        for (int i=0; i<charLen; i++) {
            product = product * (line.charAt(i) - 'A'+1);
        }
        return product;
    }
}
