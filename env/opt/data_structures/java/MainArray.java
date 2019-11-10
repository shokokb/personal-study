class Node {
    int data;

    public Node(int data) {
        this.data = data;
    }
}

class Array {
    Node[] array;
    int size;

    public Array() {
        array = new Node[1000];
        size = 0;
    }

    public int size() {
        return size;
    }

    // ランダムアクセス(O(1))
    public int data(int idx) {
        return array[idx].data;
    }

    // 末尾に追加
    public void append(int data) {
        int idx = size();
        insert(idx, data);
        // System.out.println("append " + idx + " " + data);
    }

    // 挿入(O(n))
    public void insert(int idx, int data) {
        if (idx < 0 || idx > size()) {
            System.out.println("範囲外");
            return;
        }
        // 後方をずらす
        for (int i = size(); i > idx; i--) {
            array[i] = array[i - 1];
        }
        // 開いたところに新しいデータを挿入する
        array[idx] = new Node(data);
        this.size += 1;
    }

    // 削除(O(n))
    public void remove(int idx) {
        // 前方向にずらす
        if (idx < 0 || idx > size() - 1) {
            System.out.println("範囲外");
            return;
        }
        for (int i = idx; i < size(); i++) {
            array[i] = array[i + 1];
        }
        size -= 1;
    }

    public void print() {
        System.out.print("[");
        for (int i = 0; i < size(); i++) {
            System.out.print(array[i].data + " ");
        }
        System.out.print("]");
        System.out.println();
    }

}

public class MainArray {
    public static void main(String args[]) {
        Array ary = new Array();
        System.out.println("size=" + ary.size());
        ary.append(100);
        ary.append(300);
        ary.append(200);
        ary.print();
        System.out.println("size=" + ary.size());
        ary.insert(1, 400);
        ary.insert(0, 500);
        ary.print();
        System.out.println(ary.data(2));
        ary.print();
        ary.remove(3);
        ary.print();
    }
}
