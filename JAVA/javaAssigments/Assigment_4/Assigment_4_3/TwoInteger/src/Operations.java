import java.util.Scanner;

public class Operations {
    public static void main(String[] args) throws Exception {
        System.out.print("Name: Yağız Han Aslan\nStudent Num: 210208002\n\n");
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the first integer : ");
        int first = in.nextInt();

        System.out.print("Enter the second integer : ");
        int second = in.nextInt();

        int sum = first + second;

        System.out.printf("Sum: %d\n", sum);

        int difference = first - second;
        System.out.printf("Difference: %d\n", difference);
 
        int product = first * second;
        System.out.printf("Product: %d\n", product);

        double average = (first + second) / 2.0;
        System.out.printf("Average: %f\n", average);

        int distance = Math.abs(difference);
        System.out.printf("Distance: %d\n", distance);

        int max = Math.max(first, second);
        System.out.printf("Maximum: %d\n", max);

        int min = Math.min(first, second);
        System.out.printf("Minimum: %d\n", min);
    }
}
