// 集合
interface Aggregate {
    public abstract Iterator Iterator();
}

// 反復子
interface Iterator {
    public abstract Object next();

    public abstract boolean hasNext();
}

class BookShelf implements Aggregate {
    private Book[] books;
    private int last;
    private int maxSize;

    public Iterator Iterator() {
        return new BookShelfIterator(this);
    }

    public BookShelf(int maxSize) {
        this.books = new Book[maxSize];
        last = 0;
        this.maxSize = maxSize;
    }

    public Book getBookAt(int index) {
        return this.books[index];
    }

    public int getLength() {
        return this.books.length;
    }

    public void appendBook(Book book) {
        if (last < maxSize) {
            this.books[last] = book;
            last += 1;
        }
    }
}

class BookShelfIterator implements Iterator {
    private BookShelf bookShelf;
    private int index;

    public BookShelfIterator(BookShelf bs) {
        this.bookShelf = bs;
        this.index = 0;
    }

    public Object next() {
        Book book = bookShelf.getBookAt((index));
        index += 1;
        return book;
    }

    public boolean hasNext() {
        return (index < bookShelf.getLength());
    }
}

class Book {
    private String name = "";

    Book(String name) {
        this.name = name;
    }

    String getName() {
        return name;
    }
}

public class MainIterator {
    public static void main(String args[]) {
        BookShelf bs = new BookShelf(4);
        bs.appendBook(new Book("Book1"));
        bs.appendBook(new Book("Book2"));
        bs.appendBook(new Book("Book3"));
        bs.appendBook(new Book("Book4"));
        bs.appendBook(new Book("Book5"));

        Iterator iterator = new BookShelfIterator(bs);

        while (iterator.hasNext()) {
            Book book = (Book) iterator.next();
            System.out.println(book.getName());
        }
    }
}