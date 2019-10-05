class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }

    public int GetData() {
        return data;
    }
}

class List {
    Node head = null;

    public List() {
        this.head = null;
    }

    public int size() {
        int size = 0;
        Node temp = this.head;
        while (temp != null) {
            size += 1;
            temp = temp.next;
        }
        return size;
    }

    public void append(int data) {
        Node temp = head;
        if (head == null) {
            head = new Node(data);
        } else {
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = new Node(data);
        }
    }

    // 挿入(O(1))
    public void insert(int idx, int data) {
        // 元のnode[idx](temp) -> node[idx + 1]となり
        // newNode -> node[idx]となる
        // newNodeはtempをさすようになり、tempの1つ前はnewNodeをさすようになる
        // 先頭の場合はnewNodeはheadを指すようになる
        Node newNode = new Node(data);
        if (idx == 0) {
            newNode.next = this.head;
            this.head = newNode;
        } else if (0 < idx && idx < this.size()) {
            int i = 0;
            Node prev = this.head;
            while (prev != null) {
                // i番目の要素
                if (i == idx - 1) {
                    newNode.next = prev.next;
                    prev.next = newNode;
                    break;
                }
                prev = prev.next;
                i += 1;
            }
        } else {
            System.out.println("範囲外");
        }
    }

    public void remove(int idx) {
        // node[idx-1](temp) -> node[idx + 1]となり
        // 先頭の場合はheadはhead.next.nextを指すようになる
        if (idx == 0) {
            // 0の場合は先頭を見つけることができない為、分岐する
            this.head = this.head.next;
        } else if (0 < idx && idx < this.size()) {
            int i = 0;
            Node prev = this.head;
            while (prev != null) {
                if (i == idx - 1) {
                    // 削除O(1)
                    prev.next = prev.next.next;
                    break;
                }
                prev = prev.next;
                i += 1;
            }
        } else {
            System.out.println("範囲外");
        }
    }

    public void print() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

}

public class MainList {
    public static void main(String args[]) {
        List l = new List();
        l.append(100);
        l.append(300);
        l.append(200);
        l.insert(1, 400);
        l.insert(0, 500);
        l.print();
        l.remove(3);
        l.print();
    }
}
