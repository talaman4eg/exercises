import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private static final double CONFIDENCE_95 = 1.96;

    private final int trials;
    private final double[] results;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("n and trials must be positive, n=" + n
                    + ", trials=" + trials + " received");
        }
        this.trials = trials;
        this.results = new double[trials];

        for (int tr = 0; tr < this.trials; tr++) {
            Percolation p = new Percolation(n);
            while (!p.percolates()) {
                int col = StdRandom.uniform(n) + 1;
                int row = StdRandom.uniform(n) + 1;
                while (p.isOpen(row, col)) {
                    col = StdRandom.uniform(n) + 1;
                    row = StdRandom.uniform(n) + 1;
                }
                p.open(row, col);
            }
            this.results[tr] = p.numberOfOpenSites() * 1.0 / (n * n);
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(this.results);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(this.results);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return this.mean() - PercolationStats.CONFIDENCE_95 * this.stddev() / Math.sqrt(this.trials);
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return this.mean() + PercolationStats.CONFIDENCE_95 * this.stddev() / Math.sqrt(this.trials);
    }

    // test client (see below)
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        // Stopwatch sw = new Stopwatch();
        PercolationStats ps = new PercolationStats(n, trials);
        // double elpTime = sw.elapsedTime();
        StdOut.println(String.format("mean                    = %f", ps.mean()));
        StdOut.println(String.format("stddev                  = %f", ps.stddev()));
        StdOut.println(String.format("95%% confidence interval = [%f, %f]", ps.confidenceLo(), ps.confidenceHi()));
        // StdOut.println(String.format("Elapsed time            = %f", elpTime));

    }

}
