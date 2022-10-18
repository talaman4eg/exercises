import edu.princeton.cs.algs4.StdOut;

import java.util.Iterator;

public class Deque<Item> implements Iterable<Item> {

    private Node first = null;
    private Node last = null;

    private int size = 0;

    private class Node {
        Item item;
        Node next;
        Node previous;
    }

    // construct an empty deque
    public Deque() {

    }

    // is the deque empty?
    public boolean isEmpty() {
        return this.size == 0;
    }

    // return the number of items on the deque
    public int size() {
        return this.size;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) {
            throw new IllegalArgumentException("item cannot be null");
        }
        Node newNode = new Node();
        newNode.item = item;
        newNode.next = this.first;
        this.first = newNode;
        if (this.isEmpty()) {
            this.last = newNode;
        } else if (this.first.next != null) {
            this.first.next.previous = this.first;
        }
        this.size++;
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) {
            throw new IllegalArgumentException("item cannot be null");
        }
        Node newNode = new Node();
        newNode.item = item;
        newNode.previous = this.last;
        this.last = newNode;
        if (this.isEmpty()) {
            this.first = newNode;
        } else if (this.last.previous != null) {
            this.last.previous.next = this.last;
        }
        this.size++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (this.isEmpty()) {
            throw new java.util.NoSuchElementException("Cannot remove from empty queue");
        }
        Item res = this.first.item;
        this.first = this.first.next;
        this.size--;
        if (this.isEmpty()) {
            this.last = null;
        } else {
            this.first.previous = null;
        }
        return res;
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (this.isEmpty()) {
            throw new java.util.NoSuchElementException("Cannot remove from empty queue");
        }
        Item res = this.last.item;
        this.last = this.last.previous;
        this.size--;
        if (this.isEmpty()) {
            this.first = null;
        } else {
            this.last.next = null;
        }
        return res;

    }

    private class DequeueIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return this.current != null;
        }

        public void remove() {
            throw new UnsupportedOperationException("Method not implemented");
        }

        public Item next() {
            if (!this.hasNext()) {
                throw new java.util.NoSuchElementException("No next element");
            }
            Item res = this.current.item;
            this.current = this.current.next;
            return res;
        }
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new DequeueIterator();
    }

    // unit testing (required)
    public static void main(String[] args) {

        String item;
        Deque<String> dq = new Deque<>();
        assert dq.isEmpty();
        assert dq.size() == 0;
        dq.addFirst("Only");
        assert !dq.isEmpty();
        assert dq.size() == 1;
        item = dq.removeFirst();
        assert item.equals("Only");
        assert dq.isEmpty();
        assert dq.size() == 0;

        dq.addFirst("Only");
        item = dq.removeLast();
        assert item.equals("Only");
        assert dq.size() == 0;
        assert dq.isEmpty();

        dq.addLast("Only");
        assert !dq.isEmpty();
        assert dq.size() == 1;
        item = dq.removeLast();
        assert item.equals("Only");
        assert dq.size() == 0;

        dq.addLast("Only");
        item = dq.removeFirst();
        assert item.equals("Only");
        assert dq.size() == 0;
        assert dq.isEmpty();

        dq.addFirst("First");
        assert dq.size() == 1;
        dq.addFirst("Second");
        assert dq.size() == 2;
        dq.addFirst("Third");
        assert dq.size() == 3;

        item = dq.removeFirst();
        assert item.equals("Third");
        assert dq.size() == 2;
        item = dq.removeLast();
        assert item.equals("First");
        assert dq.size() == 1;
        item = dq.removeLast();
        assert item.equals("Second");
        assert dq.size() == 0;
        assert dq.isEmpty();

        dq.addLast("First");
        assert dq.size() == 1;
        dq.addLast("Second");
        assert dq.size() == 2;
        dq.addLast("Third");
        assert dq.size() == 3;

        item = dq.removeFirst();
        assert item.equals("First");
        assert dq.size() == 2;
        item = dq.removeLast();
        assert item.equals("Third");
        assert dq.size() == 1;
        item = dq.removeFirst();
        assert item.equals("Second");
        assert dq.size() == 0;
        assert dq.isEmpty();


        String[] lst = {
                "First", "Second", "Third", "Fourth", "Fifth"
        };
        for (String s : lst) {
            dq.addLast(s);
        }
        assert dq.size() == lst.length;

        var ind = 0;
        for (String s : dq) {
            assert s.equals(lst[ind]);
            StdOut.println(s);
            ind++;
        }
        assert ind == lst.length;
        /*

        dq = null;

        int testSize = 100;
        int[] testData = new int[testSize];
        for (int i = 0; i < testSize; i++) {
            testData[i] = i;
        }

        Deque<Integer> dq1 = new Deque<Integer>();
        int[] comdData = new int[testSize];

        for (int i = 0; i < testSize; i++) {

        }

         */


    }

}
