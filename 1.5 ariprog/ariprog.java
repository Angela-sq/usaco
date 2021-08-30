/*
ID: angela.14
LANG: JAVA
TASK: ariprog
*/
import java.io.*;
import java.util.*;

public class ariprog {
    public static void main(String[] args) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("ariprog.in"));
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));
        int N = Integer.parseInt(fin.readLine());
        int M = Integer.parseInt(fin.readLine());

        int max = M * M * 2;
        boolean[] bisquares = new boolean[max + 1];
        ArrayList<int[]> results = new ArrayList<>();
        for (int p = 0; p <= M; p++) {
            for (int q = 0; q <= M; q++) {
                bisquares[p * p + q * q] = true;
            }
        }

        for (int i = 0; i < max; i++) {
            if (!bisquares[i])
                continue;
            diffLoop: for (int j = 1; j <= (max - i) / (N - 1); j++) {
                for (int k = 1; k <= N - 1; k++) {
                    if (!bisquares[i + j * k])
                        continue diffLoop;
                }
                results.add(new int[] { i, j });
            }
        }

        if (results.size() > 1) {
            Collections.sort(results, new Comparator<int[]>() {
                public int compare(int[] prog1, int[] prog2) {
                    int compTerms = prog1[1] - prog2[1];
                    if (compTerms != 0) {
                        return compTerms;
                    }
                    return prog1[0] - prog2[0];
                }
            });
        }

        if (results.size() > 0) {
            for (int[] result : results) {

                fout.println(result[0] + " " + result[1]);
            }
        } else {
            fout.println("NONE");
        }
        fout.close();
    }

}