import java.util.Arrays;
import java.util.List;

public class MergeSort <E>{
    E[] array;
    public MergeSort(E[] array){
        this.array = array;

    }
    public MergeSort(){

    }
    public void print(int[] array){
        for (int i = 0; i < array.length; i ++){
            System.out.print(array[i] + " ");
        }

    }
    public int[] sort(int[] array) {
        if (array.length == 1)
            return array;
        int[] temp1 = Arrays.copyOfRange(array, 0, (array.length) / 2);
        int[] temp2 = Arrays.copyOfRange(array, (array.length) / 2, array.length);
        int[] newArray = new int[temp1.length + temp2.length];
        sort(temp1);
        System.out.println(temp1.length + " length");
        sort(temp2);
        int x = 0;
        int y = 0;
        int i = 0;
        while (x < temp1.length && y < temp2.length) {
            if (temp1[x] < temp2[y]) {
                newArray[i] = temp1[x];
                x++;
                i++;
            }
            else {
                newArray[i] = temp2[y];
                y++;
                i++;
            }
        }
        while (x < temp1.length){
            newArray[i] = temp1[x];
            x++;
            i++;
        }
        while (y < temp1.length){
            newArray[i] = temp1[y];
            y++;
            i++;
        }
        print(newArray);
        System.out.print("\n");



        return newArray;



    }
    public static void main(String args[]){
        int[] x = {3, 100, 8, 7, 12, 4, 15, 35, 80, 61, 72, 69};
        MergeSort a = new MergeSort();
        x = a.sort(x);
        a.print(x);

    }

}
