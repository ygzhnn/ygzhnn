import java.util.Scanner;

public class Power {
    
    public static void main(String[] args) throws Exception {
        System.out.print("Name: Yağız Han Aslan\nStudent Num: 210208002\n\n");
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a number : ");
        double num = in.nextDouble();

        double square = num * num;
        double cube = num * num * num;
        double fourth = num * num * num *num;

        System.out.print("Square of this number : "+square+"\n"+"Cube of this number : "+cube+"\n"+"Fourth power of this number : "+fourth);
    }
}
