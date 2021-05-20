package applications.arithmetic;

/**
 * this interface define the structure of a evaluator.
 * @author Jason Zhang
 * id:112710259
 * CSE 214
 */


public interface Evaluator {
    /**
     *
     * @param expressionString expression
     * @return the value of the expression
     */
    double evaluate(String expressionString);


    class TokenBuilder {

        /**
         * The {@link StringBuilder} object used internally. This is used because {@link String}s in
         * Java are immutable, while we may want to build a token as we parse from left to right one
         * character at a time.
         */
        private StringBuilder tokenBuilder = new StringBuilder();

        /**
         * @see StringBuilder#append(char)
         */
        public void append(char c) {
            tokenBuilder.append(c);
        }

        /**
         * @return the final string object that represents a single token
         * @see StringBuilder#toString()
         */
        public String build() {
            return tokenBuilder.toString();
        }

    }
    String nextToken(String s, int start);

    /**
     * Determines whether or not a string is a valid operand.
     *
     * @param s the given string
     * @return <code>true</code> if the given string is a valid operand, and <code>false</code> otherwise
     */
    boolean isOperand(String s);

    /**
     * This class handles the parsing of tokens from a string. This is helpful in situations where a
     * single token may take up more than one character in the string.
     */

}
