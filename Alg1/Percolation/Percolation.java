import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private final int n;
    private final boolean[][] matrix;
    private int numOpenSites = 0;

    private final WeightedQuickUnionUF qufPerc;
    // private QuickFindUF qufPerc;
    private final WeightedQuickUnionUF qufIsFull;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("n must be positive, n=" + n + " received");
        }
        this.n = n;
        this.matrix = new boolean[this.n][this.n];
        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.n; j++) {
                this.matrix[i][j] = false;
            }
        }
        this.numOpenSites = 0;

        // this.qufPerc = new QuickFindUF(this.n * this.n + 2);
        this.qufPerc = new WeightedQuickUnionUF(this.n * this.n + 2);
        this.qufIsFull = new WeightedQuickUnionUF(this.n * this.n + 2);

        for (int i = 1; i <= this.n; i++) {
            // this.qufPerc.union(0, i);
            this.qufIsFull.union(0, i);
            // this.qufPerc.union(this.n * this.n + 1, this.n * this.n + 1 - i);
        }

    }

    private int flatten(int row, int col) {
        this.validateRowCol(row, col);
        return (row - 1) * this.n + col;
    }

    private void validateRowCol(int row, int col) {
        if (row <= 0 || row > this.n || col <= 0 || col > this.n) {
            throw new IllegalArgumentException("row and col must be positive and less or equal than n=" + this.n + ", row=" + row + ", col=" + col + " received");
        }
    }


    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        this.validateRowCol(row, col);
        if (!this.isOpen(row, col)) {
            this.numOpenSites += 1;
        }
        this.matrix[row - 1][col - 1] = true;

        if (row > 1) {
            if (this.isOpen(row - 1, col)) {
                this.qufPerc.union(this.flatten(row, col), this.flatten(row - 1, col));
                this.qufIsFull.union(this.flatten(row, col), this.flatten(row - 1, col));
            }
        } else {
            this.qufPerc.union(this.flatten(row, col), 0);
        }
        if (row < this.n) {
            if (this.isOpen(row + 1, col)) {
                this.qufPerc.union(this.flatten(row, col), this.flatten(row + 1, col));
                this.qufIsFull.union(this.flatten(row, col), this.flatten(row + 1, col));
            }
        } else {
            this.qufPerc.union(this.flatten(row, col), this.n * this.n + 1);
        }
        if (col > 1) {
            if (this.isOpen(row, col - 1)) {
                this.qufPerc.union(this.flatten(row, col), this.flatten(row, col - 1));
                this.qufIsFull.union(this.flatten(row, col), this.flatten(row, col - 1));
            }
        }
        if (col < this.n) {
            if (this.isOpen(row, col + 1)) {
                this.qufPerc.union(this.flatten(row, col), this.flatten(row, col + 1));
                this.qufIsFull.union(this.flatten(row, col), this.flatten(row, col + 1));
            }
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        this.validateRowCol(row, col);
        return this.matrix[row - 1][col - 1];

    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        return this.isOpen(row, col) &&
                (
                        this.qufIsFull.find(0) == this.qufIsFull.find(this.flatten(row, col))
                        // || this.qufPerc.find(this.n * this.n + 1) == this.qufPerc.find(this.flatten(row, col))
                );

    }

    // returns the number of open sites
    public int numberOfOpenSites() {

        return this.numOpenSites;
    }

    // does the system percolate?
    public boolean percolates() {
        return this.qufPerc.find(0) == this.qufPerc.find(this.n * this.n + 1);
    }

    // test client (optional)
    public static void main(String[] args) {
        int n = 5;

        Percolation p = new Percolation(n);

        int numOpenSites = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                assert !p.isOpen(i, j);
                assert !p.isFull(i, j);
            }
        }
        assert p.numberOfOpenSites() == 0;


        p.open(1, 1);
        assert p.isOpen(1, 1);
        assert p.isFull(1, 1);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(1, 3);
        assert p.isOpen(1, 3);
        assert p.isFull(1, 3);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(5, 1);
        assert p.isOpen(5, 1);
        assert !p.isFull(5, 1);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(5, 2);
        assert p.isOpen(5, 2);
        assert !p.isFull(5, 2);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(5, 3);
        assert p.isOpen(5, 3);
        assert !p.isFull(5, 3);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(2, 2);
        assert p.isOpen(2, 2);
        assert !p.isFull(2, 2);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(2, 1);
        assert p.isOpen(2, 1);
        assert p.isFull(2, 1);
        assert p.isFull(2, 2);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();


        p.open(2, 4);
        assert p.isOpen(2, 4);
        assert !p.isFull(2, 4);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(3, 4);
        assert p.isOpen(3, 4);
        assert !p.isFull(3, 4);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(3, 3);
        assert p.isOpen(3, 3);
        assert !p.isFull(3, 3);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(4, 3);
        assert p.isOpen(4, 3);
        assert !p.isFull(4, 3);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(4, 4);
        assert p.isOpen(4, 4);
        assert !p.isFull(4, 4);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(4, 5);
        assert p.isOpen(4, 5);
        assert !p.isFull(4, 5);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(5, 4);
        assert p.isOpen(5, 4);
        assert !p.isFull(5, 4);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert !p.percolates();

        p.open(2, 3);
        assert p.isOpen(2, 3);
        assert p.isFull(2, 3);
        numOpenSites++;
        assert p.numberOfOpenSites() == numOpenSites;
        assert p.percolates();


        assert p.isFull(4, 5);
        assert p.isFull(4, 4);
        assert p.isFull(4, 3);
        assert p.isFull(3, 3);
        assert p.isFull(3, 4);
        assert p.isFull(2, 4);

        assert p.isFull(5, 1);
        assert p.isFull(5, 2);
        assert p.isFull(5, 3);
        assert p.isFull(5, 4);


    }
}
