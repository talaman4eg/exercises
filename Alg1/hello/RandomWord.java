/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String champion = "";
        double j = 1;
        while (!StdIn.isEmpty()) {
            String line = StdIn.readString();
            if (StdRandom.bernoulli(1 / j)) {
                champion = line;
            }
            j += 1;

        }
        StdOut.println(champion);
    }
}
