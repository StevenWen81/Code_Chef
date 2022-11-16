import java.util.Scanner;

class Which_Division {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int index = input.nextInt();
        for (int i = 0; i < index; i++)
        {
            int number = input.nextInt();
            if (2000 <= number)
            {
                System.out.println(1);
            }
            if (1600<=number && number<2000)
            {
                System.out.println(2);
            }
            if (number < 1600)
            {
                System.out.println(3);
            }
        }
        input.close();
    }
}