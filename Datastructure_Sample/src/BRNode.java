public class BRNode {
    BRNode parent, leftChild, rightChild;
    int data;
    color rb;
    public BRNode(){
        rb = color.BlACK;
        leftChild = null;
        rightChild = null;
    }


    public BRNode(int data){
        this.data = data;
        leftChild = null;
        rightChild = null;
        parent = null;
        rb = color.RED;


    }
    public static void main(String[] args){
        BRNode a = new BRNode();
        System.out.print(a.leftChild.rb);
    }
}
