import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Permutation {

    /*    private static void permDeq(String[] args) {
            if (args.length == 0) {
                return;
            }
            Deque<String> q = new Deque<>();
            for (String arg : args) {
                if (StdRandom.bernoulli()) {
                    q.addFirst(arg);
                } else {
                    q.addLast(arg);
                }
            }

            for (String str : q) {
                StdOut.println(q.removeFirst());
            }

        }
    */
/*    private static void permRandQueue(String[] args) {
        RandomizedQueue<String> q = new RandomizedQueue<>();
        for (String arg : args) {
            q.enqueue(arg);
        }

        for (String str : q) {
            StdOut.println(str);
        }

    }
*/
    public static void main(String[] args) {
        if (args.length == 0) {
            return;
        }
        // Permutation.permRandQueue(args);
        RandomizedQueue<String> q = new RandomizedQueue<>();
        int k = Integer.parseInt(args[0]);

        while (!StdIn.isEmpty()) {
            q.enqueue(StdIn.readString());
        }

        if (k > 0) {
            int i = 0;
            for (String str : q) {
                StdOut.println(str);
                i++;
                if (i >= k) {
                    break;
                }
            }
        }
    }
}
