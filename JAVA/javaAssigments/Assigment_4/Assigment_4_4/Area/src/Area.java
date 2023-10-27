import java.util.Scanner;

public class Area {
    public static void main(String[] args) throws Exception {
        System.out.print("Name: Yağız Han Aslan\nStudent Num: 210208002\n\n");
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the height of rectangle : ");
        int height = in.nextInt();

        System.out.print("Enter the widht of rectangle : ");
        int widht = in.nextInt();

        int area = widht * height;
        int perimeter = 2*widht + 2*height;
        double diagonal = Math.sqrt(Math.pow(widht, 2) + Math.pow(height, 2));

        System.out.print("Area of rectangle : "+area+"\n"+"Perimeter of rectangle : "+perimeter+"\n"+"Lenght of rectangles diagonal : "+diagonal);


    
    }
}
