import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class RandomizedQueue<Item> implements Iterable<Item> {

    private int size = 0;
    private Item[] items;

    // construct an empty randomized queue
    public RandomizedQueue() {
        this.items = (Item[]) new Object[1];
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return this.size == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        return this.size;
    }

    private void checkArraySize() {
        int newSize = 0;
        if (this.size() == this.items.length) {
            newSize = this.items.length * 2;
        } else if (this.size() > 0 && this.size() <= this.items.length / 4) {
            newSize = this.items.length / 2;
        } else {
            return;
        }
        Item[] newItems = (Item[]) new Object[newSize];
        for (int i = 0; i < this.size(); i++) {
            newItems[i] = this.items[i];
        }
        this.items = newItems;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException("Item cannot be null");
        }
        this.checkArraySize();
        this.items[this.size++] = item;
    }

    private int getRandomIndex() {
        return StdRandom.uniform(this.size());
    }

    // remove and return a random item
    public Item dequeue() {
        if (this.isEmpty()) {
            throw new NoSuchElementException("Cannot dequeue from empty queue");
        }
        int index = this.getRandomIndex();
        Item result = this.items[index];
        this.items[index] = this.items[this.size - 1];
        this.items[--this.size] = null;
        this.checkArraySize();
        return result;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (this.isEmpty()) {
            throw new NoSuchElementException("Cannot sample from empty queue");
        }
        int index = this.getRandomIndex();
        return this.items[index];
    }

    private class RandomizedQueueIterator implements Iterator<Item> {
        private final Item[] iterItems;
        private int currentIndex = 0;

        public RandomizedQueueIterator() {
            this.iterItems = (Item[]) new Object[size];
            int i = 0;
            for (int ind : StdRandom.permutation(size)) {
                this.iterItems[i] = items[ind];
                i++;
            }
        }

        public boolean hasNext() {
            return this.currentIndex < this.iterItems.length;
        }

        public void remove() {
            throw new UnsupportedOperationException("Method not implemented");
        }

        public Item next() {
            if (!this.hasNext()) {
                throw new NoSuchElementException("No next element");
            }
            return this.iterItems[this.currentIndex++];
        }

    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new RandomizedQueueIterator();
    }

    // unit testing (required)
    public static void main(String[] args) {
        RandomizedQueue<String> rq = new RandomizedQueue<String>();
        assert rq.isEmpty();
        assert rq.size() == 0;
        rq.enqueue("Only");
        assert !rq.isEmpty();
        assert rq.size() == 1;

        assert rq.sample().equals("Only");
        assert !rq.isEmpty();
        assert rq.size() == 1;

        String res = rq.dequeue();
        assert res.equals("Only");
        assert rq.isEmpty();
        assert rq.size() == 0;

        rq.enqueue("1");
        rq.enqueue("2");
        rq.enqueue("3");
        rq.enqueue("4");
        rq.enqueue("5");
        assert !rq.isEmpty();
        assert rq.size() == 5;


        StdOut.println("sample [1:5]:");
        StdOut.println(rq.sample());
        StdOut.println(rq.sample());
        StdOut.println(rq.sample());

        StdOut.println("dequeue[1:5]:");
        StdOut.println(rq.dequeue());
        StdOut.println(rq.dequeue());
        StdOut.println(rq.dequeue());
        assert !rq.isEmpty();
        assert rq.size() == 2;

        StdOut.println(rq.dequeue());
        StdOut.println(rq.dequeue());
        assert rq.isEmpty();
        assert rq.size() == 0;

        rq.enqueue("1");
        rq.enqueue("2");
        rq.enqueue("3");
        rq.enqueue("4");
        rq.enqueue("5");

        StdOut.println("First iter[1:5]:");
        for (String str : rq) {
            StdOut.println(str);
        }
        StdOut.println("Second iter[1:5]:");
        for (String str : rq) {
            StdOut.println(str);
        }
    }

}
