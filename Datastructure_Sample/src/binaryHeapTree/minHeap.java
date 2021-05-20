package binaryHeapTree;

public class minHeap {
    public static boolean checkMinHeap(int[] array, int i)
    {
        if (2*i + 2 > array.length) {
            return true;
        }
        boolean left = (array[i] <= array[2*i + 1]) && checkMinHeap(array, 2*i + 1);

        boolean right = (2*i + 2 == array.length) || (array[i] <= array[2*i + 2] && checkMinHeap(array, 2*i + 2));

        return left && right;
    }
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4};
        System.out.print(checkMinHeap(array, 0));
    }


}
