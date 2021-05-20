package applications.arithmetic;

import datastructures.sequential.SNode;
import datastructures.sequential.Stack;

/**
 * This class evaluate the postfix expression and return the evaluation as a double
 * @author Jason Zhang
 * id:112710259
 * CSE 214
 */


public class PostfixEvaluator implements Evaluator {
    @Override
    /**
     * this method evaluate the postfix expression and return it as double
     * @param operand create a stack data structure to store operand
     * @param expression store the postfix expression
     * @return return the evaluated value in double.
     **/
    public double evaluate(String expressionString){
        Stack operand = new Stack();
        String expression = expressionString;
        while (expression.length() != 0) {
            String temp = nextToken(expression, 0);
            if (temp == " ")
                expression = expression.substring(1);

            else if (isOperand(temp) == true) {
                operand.push(new SNode(temp));
                expression = expression.substring(expression.length() - (expression.length() - temp.length() - 1));
            } else {
                double tempnum2 = Double.parseDouble((String) operand.pop().getData());
                double tempnum1 = Double.parseDouble((String) operand.pop().getData());
                operand.push(new SNode("" + operation(tempnum1, tempnum2, temp.charAt(0))));
                expression = expression.substring(1);
            }

        }
        return Double.parseDouble((String) operand.peek().getData());

    }

    /**
     * this method perform the operation of the postfix expression in infix between two operand
     * @param a first Operand
     * @param b second Operand
     * @param s the operator
     * @return evaluate a operator b
     */

    public double operation(double a, double b, char s) {
        switch (s) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return a / b;
            default:
                System.out.print("No such operator");
                return 0;
        }
    }

    /**
     * this method give a operand or a operator from the expression
     * @param s the expression
     * @param start where to start at the string
     * @return a operand or a operator
     */

    @Override
    public String nextToken(String s, int start) {
        Converter.TokenBuilder a = new Converter.TokenBuilder();
        if (s.length() == 0)
            return "";
        else if (s.charAt(0) == ' ')
            return " ";
        if (Operator.isOperator(s.charAt(0)))
            a.append(s.charAt(0));
        else {
            while (start < s.length()) {
                if (Operator.isOperator(s.charAt(start)) || s.charAt(start) == ' ')
                    break;
                a.append(s.charAt(start));
                start++;

            }
        }
        return a.build();
    }

    /**
     * this method check if the string is a valid operand or not
     * @param s the given string
     * @return true or false if the string is a operand
     */

    @Override
    public boolean isOperand(String s) {
        if (s.length() == 0)
            return true;
        else if (Operator.isOperator(s) == true)
            return false;
        return isOperand(s.substring(1));
    }
}
