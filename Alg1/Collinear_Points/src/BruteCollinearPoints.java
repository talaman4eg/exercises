import java.util.Arrays;

public class BruteCollinearPoints {
    // finds all line segments containing 4 points

    Point[] points;

    public BruteCollinearPoints(Point[] points) throws IllegalAccessException {
        if (points == null) {
            throw new IllegalAccessException("points cannot be null");
        }
        this.points = points;
        Arrays.sort(this.points);
        Point prev = null;
        for (Point p : this.points) {
            if (p == null) {
                throw new IllegalAccessException("all points must be not null");
            }
            if (p.equals(prev)) {
                throw new IllegalAccessException("all points must be different");
            }
            prev = p;
        }

    }

    // the number of line segments
    public int numberOfSegments() {

    }

    // the line segments
    public LineSegment[] segments() {

    }
}
