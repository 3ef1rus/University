import java.util.Scanner;

public class Calculator {
    static Scanner scanner = new Scanner(System.in);

    public static int getInt() {
        System.out.println("Введите число:");
        Integer num;
        String s = scanner.nextLine();
        num = Integer.parseInt(s);
        if (num instanceof Integer) {
            return num;
        } else {
            System.out.println("Ошибка, Повторите.");
            scanner.next();// рекурсия
            num = getInt();
        }
        return num;
    }

    public static char getOperation() {
        System.out.println("Введите операцию:");
        char operation;
        if (scanner.hasNext()) {
            operation = scanner.next().charAt(0);
        } else {
            System.out.println("Ошибка, Повторите.");
            scanner.next();// рекурсия
            operation = getOperation();
        }
        return operation;
    }

    public static int calc(int num1, int num2, char operation) {
        int result;
        switch (operation) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = num1 / num2;
                break;
            case '^':
                result = (int) Math.pow(num1, num2);
                break;
            default:
                System.out.println("Ошибка. Повторите ввод.");
                result = calc(num1, num2, getOperation());// рекурсия
        }
        return result;
    }

    public static void main(String[] args) {
        Object a = Integer.max(123, 23);
        int num1 = getInt();
        int num2 = getInt();
        char operation = getOperation();
        int result = calc(num1, num2, operation);
        System.out.println("Результат операции: " + result);
        System.out.println("Максимальное число а:" + a);
        a=null;
        System.gc();
        System.out.println("Сборщик мусора произвел зачистку");
    }

}