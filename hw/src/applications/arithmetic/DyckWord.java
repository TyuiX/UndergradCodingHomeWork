package applications.arithmetic;

/**
 * This class is to check if the expression is a valid Dyck word or not
 * @author Jason Zhang
 * id:112710259
 * CSE 214
 */


public class DyckWord {

    private final String word;

    /**
     *
     * @param word the expression
     */

    public DyckWord(String word) {
        if (isDyckWord(word))
            this.word = word;
        else
            throw new IllegalArgumentException(String.format("%s is not a valid Dyck word.", word));
    }

    /**
     *This method check if the expression is a dyck word or not
     * @param word the expression
     * @return true or false if the expression is dyckword or not
     */

    private static boolean isDyckWord(String word) {
        // todo
        if (word.length() == 0)
            return true;
        else if (Brackets.isRightBracket(word) == true)
            return false;
        else if (Brackets.isLeftBracket(word) == false)
            return isDyckWord(word.substring(1));
        for (int i = 1; i < word.length(); i++) {
            if (Brackets.isLeftBracket(word.charAt(i))== true){
                int x = isDyckWordhelper(word.substring(i));
                if (x == 0)
                    return false;
                i += x;

            }
            else if (Brackets.isRightBracket(word.charAt(i)) == true) {
                if (Brackets.correspond(word.charAt(0), word.charAt(i))) {
                    if (i + 1 < word.length())
                        return isDyckWord(word.substring(i+1));
                    else
                        return true;
                }
                else
                    return false;

            }
        }

        return false;
    }

    /**
     * this method give the length of a valid dyck word in the expression to help with the main method
     * @param word remaining character of the expression
     * @return the length of the valid dyckword inside the bracket, if it not return 0
     */
    // help if left bracket show up during for loop and get the length of the string.
    private static int isDyckWordhelper(String word){
        int x = 1;
        while (Brackets.correspond(word.charAt(0), word.charAt(x))== false) {
            if (Brackets.isLeftBracket(word.charAt(x))){
                int y = isDyckWordhelper(word.substring(x));
                if (y == 0) {
                    x = 0;
                    break;
                }
                else
                    x += y;
            }
            x++;
            if (x == word.length()){
                x = 0;
                break;
            }
        }
        return x;

    }

    /**
     * give the dyck word
     * @return Dyck word
     */

    public String getWord() {
        return word;
    }

}
