package binaryHeapTree;

public interface maxHeapTree<T> {
    /***
     * insert element into the array
     * @param element
     */
    void insert(int element);

    void delete(int index);

    /**
     * find the max data
     */

    int getMax();

    /**
     * delete the min data
     */

    void removeMax();

    void resize();


}
