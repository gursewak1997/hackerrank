/*
Link to the problem:

https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

*/
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class newYearChaos {

    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
        int swap = 0;
        int bribes;
        int position = 0;
        for(int i = q.length-1; i >= 0; i--) {
            int j = 0;

            bribes = q[position] - (position+1);
            if (bribes > 2) {
                System.out.println("Too chaotic");
                return;
            }
            if (q[i] - 2 > 0){
                j = q[i] - 2;
            }
            
            while(j <= i) {
                if (q[j] > q[i]){
                    swap++;
                }
                j++;
            }
            position++;
        }
        System.out.println(swap);

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] q = new int[n];

            String[] qItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qItems[i]);
                q[i] = qItem;
            }

            minimumBribes(q);
        }

        scanner.close();
    }
}
