import java.util.Scanner;

public class VendingMachine {
    public static void main(String[] args) throws Exception {
                  System.out.print("Name: Yağız Han Aslan\nStudent Num: 210208002\n\n");
                  Scanner in = new Scanner(System.in);
                  int perDollar = 100;
      
                  int perQuarter = 25;
      
                  System.out.print("Enter bill value (1 = $1 , 5 = $5): ");
                  int bill = in.nextInt();
      
                  System.out.print("Enter the price in pennies: ");
                  int price = in.nextInt();
      
                  // Compute change due
      
                  int changeDue = perDollar * bill - price;
      
                  int dollarCoins = changeDue / perDollar;
      
                  changeDue = changeDue % perDollar;
    
                  int quarters = changeDue / perQuarter;
      
                  // Print change due
      
                  System.out.printf("Dollar: %d", dollarCoins);
                  System.out.println();

                  System.out.printf("Quarters: %d", quarters);
                  System.out.println();
      
                             
      
            }

      
      }
    

