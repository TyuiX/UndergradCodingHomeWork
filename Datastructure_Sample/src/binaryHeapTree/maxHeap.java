package binaryHeapTree;

public class maxHeap implements maxHeapTree {
    private int size = 0;
    private int[] array ;
    private int max ;


    public maxHeap(){
        array = new int[64];
    }
    public maxHeap(int size){
        array = new int[size];
    }


    @Override
    public void insert(int element) {
        if (size + 1 >= array.length) {
            resize();
        }
        if (size == 0) {
            array[0] = element;
            size++;
        }
        else if (element < array[0]){
            insertleft(element, 1, 0);

        }
        else if (element > array[0]){
            insertright(element, 2, 0);

        }
    }
    public void insertleft(int element,int currentindex, int parentindex) {
        if(array[currentindex] == 0) {
            array[currentindex] = element;
            if (array[currentindex] > array[parentindex]){
                swap(currentindex);
            }
        }

        else {
            if (element < array[currentindex]) {
                insertleft(element, parentindex * 2 + 1, currentindex);

            } else if (element > array[currentindex]) {
                insertright(element, parentindex * 2 + 2, currentindex);

            }
        }

    }
    public void insertright(int element,int currentindex, int parentindex) {
        if(array[currentindex] == 0){
            array[currentindex] = element;
            if (array[currentindex] > array[parentindex]){
                swap(currentindex);
            }

        }
        else{
            if (element < array[currentindex]){
                insertleft(element, parentindex*2+1, currentindex);

            }
            else if (element > array[currentindex]) {
                insertright(element, parentindex * 2 + 2, currentindex);
            }

        }

    }
    @Override
    public void delete(int element) {


    }

    @Override
    public int getMax() {
        return array[0];

    }

    @Override
    public void removeMax() {

    }

    @Override
    public void resize() {
    }
    public  void swap(int current){
        if (current == 0) {

        }

        else if (array[current] > array[(current-1)/2]){
            int temp = array[current];
            array[current] = array[(current-1)/2];
            array[(current-1)/2] = temp;
            swap((current-1)/2);
        }

    }
    public void printheap(){
        for (int i = 0; i < array.length; i++){
            System.out.print(array[i] + " ");
        }
    }
    public boolean checkValidMaxHeap(){
        return checkValidMaxHeap(0);

    }
    public boolean checkValidMaxHeap(int i){
        System.out.println("current: " + i);
        if (2*i + 2 > array.length){
            return true;
        }
        if (array[i] < array[2*i+1] || array[i] < array[2*i+2])
            return false;

        return checkValidMaxHeap(2*i + 1) && checkValidMaxHeap(2*i + 2);

    }

    public static void main(String[] args){
        maxHeap a = new maxHeap(7);
        a.insert(6);
        System.out.println();
        a.insert(7);
        a.insert(3);
        a.insert(10);
        a.insert(2);
        a.printheap();
        System.out.println(a.checkValidMaxHeap());



    }
}
