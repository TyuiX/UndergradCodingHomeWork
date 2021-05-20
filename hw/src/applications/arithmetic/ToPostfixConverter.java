package applications.arithmetic;
import com.sun.org.glassfish.gmbal.ParameterNames;
import datastructures.sequential.SNode;
import datastructures.sequential.Stack;

/**
 * this class convert a infix expression to a postfix expression
 * @author Jason Zhang
 *
 */

public class ToPostfixConverter implements Converter {
    /**
     * this method convert a infix expression to a post fix expression
     * @param expression  the given arithmetic expression
     * @return the converted infix as postfix
     */


    @Override
    public String convert(ArithmeticExpression expression) {
        String inFix = expression.getExpression();
        String postFix = "";
        Stack symbol = new Stack();
        while (inFix.length() != 0) {
            String temp = nextToken(inFix, 0);
            // if token is a Operator
            if (isOperand(temp) == false){
                // if the stack is empty push the operator in
                if (symbol.size() == 0)
                    symbol.push(new SNode(temp.charAt(0)));
                // if the token is a right bracket, pop the stack and add it to the postfix string till a left bracket show up
                else if (Brackets.isRightBracket(temp.charAt(0)) == true) {
                    while (Brackets.isLeftBracket((Character)symbol.peek().getData()) == false)
                        postFix += symbol.pop().getData() + " ";
                    // pop the left bracket
                    symbol.pop();
                }
                // push left bracket
                else if(Brackets.isLeftBracket(temp.charAt(0))){
                    symbol.push(new SNode(temp.charAt(0)));
                }
                // if the operator rank is greater than the previous one, pop and add the previous operator to postfix and push the new operator in.
                else if (Operator.of(temp.charAt(0)).getRank() >= Operator.of((Character) symbol.peek().getData()).getRank()) {

                    postFix += (Character)symbol.pop().getData() + " ";

                    symbol.push(new SNode<Character>(temp.charAt(0)));

                }
                // push the operator in
                else {
                    symbol.push(new SNode<Character>(temp.charAt(0)));
                }


            }
            // push the Operand into postfix
            else {
                postFix += temp + " ";
            }
            // cut out the used operator or operand
            inFix = inFix.substring(temp.length());
        }
        // print the remaining Operator in the stack
        while (symbol.isEmpty() == false)
            postFix += symbol.pop().getData() + " ";



        //@return postFix: give the final converted postFix
        return postFix;

    }

    /**
     * this method give a operand or a operator from the expression
     * @param s     the given string
     * @param start the given index
     * @return a operand or operator
     */

    @Override
    public String nextToken(String s, int start) {
        //call token builder function
        Converter.TokenBuilder a = new Converter.TokenBuilder();
        // check see if the start of the string is a operator
        if (Operator.isOperator(s.charAt(start)) || (Brackets.isLeftBracket(s.charAt(start)) || Brackets.isRightBracket(s.charAt(start)))) {
            a.append(s.charAt(start));
        }
        else {
            //add the character to the token builder till a operator show up
            while (start < s.length() && (Operator.isOperator(s.charAt(start)) == false && Brackets.isRightBracket(s.charAt(start)) == false)) {
                a.append(s.charAt(start));
                start++;

            }
        }
        // @return a.build: return the stored character in token builder as a string
        return a.build();
    }

    /**
     * this method check if the string is a valid operand or not
     * @param s the given string
     * @return true or false if the string is a operand or operator
     */

    @Override
    public boolean isOperand(String s) {
        //a empty string is a valid operand
        if (s.length() == 0)
            //@return true for a valid Operand
            return true;
        //check if the start of the string is a operator
        else if (Operator.isOperator(s.charAt(0)) == true || (Brackets.isLeftBracket(s.charAt(0)) || Brackets.isRightBracket(s.charAt(0))))
            //@return false for Operators
            return false;
        //@return isOperand:if the start not a operator, recursively check all the character of the string,
        return isOperand(s.substring(1));
    }






    }
