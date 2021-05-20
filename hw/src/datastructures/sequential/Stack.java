package datastructures.sequential;

/**
 * Stack data structure for evaluating postfix and converting infix to postfix using nodes
 * @author Jason Zhang
 * id:112710259
 * CSE 214
 */

public class Stack implements  LIFOQueue<SNode> {
    SNode top ; //cursor for tracking the top of the stack
    SNode bottom; //cursor for tracking the bottom of the stack
    int size; // keep track the size of the stack



    //constructor for creating a empty stack
    public Stack(){
        top = null;
        bottom = null;
        size = 0;
    }

    /**
     * delete node and return the node from the stack
     * @return popped node
     */

    @Override
    //deleting top node of the stack
    public SNode pop() {
        //check see if the stack is empty
        if (!isEmpty()) {
            //store the pop node in a temp variable
            SNode temp = top;
            size--;
            //for the case if the size turn to 0
            if (size == 0){
                bottom = null;
            }
            //set top as bottom
            top = bottom;
            //resetting top to the node of the node before the one that was deleted.
            for (int i = 0; i < size - 1; i++){
                top = top.getNext();

            }
            // return the pop node
            return temp;
        }
        return null;

    }

    /**
     * add the a new node into the stack
     * @param element the element to be pushed onto the top of this stack.
     */

    @Override
    //add node to the stack
    public void push(SNode element) {
        //if stack is empty, set the element as the top and bottom.
        if (top == null){
            top = element;
            bottom = element;
        }
        else{
            top.setNext(element);
            top = element;
        }
        size++;

    }

    /**
     * look at the node at top of the stack
     * @return the node at top of the stack, but don't delete
     */

    @Override
    public SNode peek() {
        return top;
    }

    /**
     * give the size of the stack
     * @return the size of the stack
     */
    @Override
    public int size() {
        return size;
    }

    /**
     * check if the stack is empty or not
     * @return true or false if the stack empty or not
     */
    @Override
    public boolean isEmpty() {
        if (top != null)
            return false;
        return true;
    }
    public static void main(String[] args){
        double x = 4;
    }
}

