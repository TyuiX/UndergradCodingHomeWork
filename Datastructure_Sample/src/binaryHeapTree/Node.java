package binaryHeapTree;

public class Node <T> {
    Node parent, leftChild, rightChild;
    T data;


    public Node(T data){
        this.data = data;
        parent = null;
        leftChild = null;
        rightChild = null;


    }
}
