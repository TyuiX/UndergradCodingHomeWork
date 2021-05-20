import com.sun.prism.paint.Color;

public class blackandred {
    BRNode root;
    Boolean x = false;
    Boolean y = x && false;

    public blackandred(){
        root = null;
    }
    public blackandred(BRNode a){
        root = a;
    }
    public void insert (BRNode node){
        if (root == null){
            root = node;
            root.rb = color.BlACK;
        }
        else {
            if (root.data > node.data){
                if(root.leftChild == null) {
                    root.leftChild = node;
                    node.parent = root;
                }
                else
                    insert(node, root.leftChild);

            }
            else{
                if (root.rightChild == null) {
                    root.rightChild = node;
                    node.parent = root;
                }
                else
                    insert(node, root.rightChild);
            }

        }


    }
    public void insert (BRNode node, BRNode parent){
        if (parent.data > node.data) {
            if (parent.leftChild == null) {
                root.leftChild = node;
                node.parent = parent;

            }
            else
                insert(node, parent.leftChild);
        }
        else{
            if(parent.rightChild == null) {
                parent.rightChild = node;
                node.parent = parent;
            }
            else
                insert(node, parent.rightChild);

        }


    }
    public void rotation(BRNode node){
        if(node.parent.parent.leftChild == node.parent && node.parent.leftChild == node) {
            if (node.parent.parent.rightChild.rb == color.BlACK || node.parent.parent.rightChild == null) {
                BRNode temp = node.parent.parent.parent;
                node.parent.parent.parent = node.parent;
                node.parent.parent.leftChild = node.parent.rightChild;
                node.parent.rightChild = node.parent.parent;
                if (temp == null)
                    node.parent.parent = null;
                else {
                    node.parent.parent = temp;
                    if (temp.rightChild == node.parent.rightChild)
                        temp.rightChild = node.parent;
                    else
                        temp.leftChild = node.parent;
                }
                node.parent.rb = color.BlACK;
                node.parent.rightChild.rb = color.RED;
            }
        }
        else if(node.parent.parent.rightChild == node.parent && node.parent.rightChild == node) {
            if (node.parent.parent.leftChild.rb == color.BlACK || node.parent.parent.leftChild == null) {
                BRNode temp = node.parent.parent.parent;
                node.parent.parent.parent = node.parent;
                node.parent.parent.rightChild = node.parent.leftChild;
                node.parent.rightChild = node.parent.parent;
                if (temp == null)
                    node.parent.parent = null;
                else {
                    node.parent.parent = temp;
                    if (temp.rightChild == node.parent.rightChild)
                        temp.rightChild = node.parent;
                    else
                        temp.leftChild = node.parent;
                }
                node.parent.rb = color.BlACK;
                node.parent.leftChild.rb = color.RED;
            }
        }
        else if (node.parent.parent.leftChild == node.parent){
            if(node.parent.parent.rightChild.rb == color.RED) {
                node.parent.rb = color.BlACK;
                node.parent.parent.rightChild.rb = color.BlACK;
                node.parent.parent.rb = color.RED;

            }
            else{
                BRNode temp = node.parent.parent;
                node.parent.parent = node;
                node.parent.rightChild = null;
                node.leftChild = node.parent;
                node.parent = temp;
                rotation(node.leftChild);
            }
        }
        else if (node.parent.parent.rightChild == node.parent){
            if(node.parent.parent.leftChild.rb == color.RED) {
                node.parent.rb = color.BlACK;
                node.parent.parent.leftChild.rb = color.BlACK;
                node.parent.parent.rb = color.RED;

            }
            else{
                BRNode temp = node.parent.parent;
                node.parent.parent = node;
                node.parent.leftChild = null;
                node.rightChild = node.parent;
                node.parent = temp;
                rotation(node.rightChild);
            }
        }
    }
    public boolean checkValid(BRNode a){
        if (a.leftChild.rb == color.RED ||a.rightChild.rb == color.RED)
            return false;
        return true;
    }

}
