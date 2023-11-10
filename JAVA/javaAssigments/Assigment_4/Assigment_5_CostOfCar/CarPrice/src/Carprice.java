import java.util.Scanner;

public class Carprice {
    public static void main(String[] args) throws Exception {
//Step 1
        Scanner in = new Scanner(System.in);

//Step 2
        System.out.print("Enter the price of the car :");
        int car_price = in.nextInt();

        System.out.print("Enter the esimated miles driven per year :");
        int miles_pyear = in.nextInt();

        System.out.print("Enter the esimated gas price :");
        float gas_price = in.nextFloat();

        System.out.print("Enter miles per gallon :");
        float miles_pgallon = in.nextFloat();

        System.out.print("Enter the esimated resale value :");
        int resale = in.nextInt();

//Step 3
        float cost = (car_price-resale)+(miles_pyear*5/miles_pgallon)*gas_price;

//Step 4
        System.out.printf("Total cost of car for 5 years is : %.2f",cost);




    }
}
