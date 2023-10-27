import java.util.Scanner;

public class Initials {
    public static void main(String[] args) throws Exception {

        System.out.print("Name: Yağız Han Aslan\nStudent Num: 210208002\n\n");
        Scanner in = new Scanner(System.in);

        System.out.print("Enter  first name : ");
        String first = in.next();
        System.out.print("Enter  second name: ");
        String second = in.next();

        String initials = first.substring(0, 1) + "/" + second.substring(0, 1);
        System.out.println(initials);

    }
}
