import java.util.Scanner;

class bank
{
    public static void main(String[] args)
    {
        int balance;
        int money;
        int cash;
        balance = 0;
        money = 0;

        System.out.println("Hello User 8157!");

        Scanner sc = new Scanner(System.in);

        System.out.println("===================");
        System.out.println("Enter an option");
        System.out.println("===================");
        System.out.println("A. Check Balance");
        System.out.println("B. Deposit");
        System.out.println("C. Withdraw");
        System.out.println("D.Previous Activity");
        System.out.println("E. Exit");
        System.out.println("===================");

        System.out.print(">> ");
        char option = sc.next().charAt(0);

        //System.out.println(option);
        while (option != 'E')
        {    
            if (option == 'A' || option == 'a')
            {
                System.out.println("Your Balance is: $" + balance);
                System.out.println("\n");

                System.out.println("=========================");
                System.out.println("Enter an option");
                System.out.println("=========================");
                System.out.println("A. Check Balance");
                System.out.println("B. Deposit");
                System.out.println("C. Withdraw");
                System.out.println("D. Exit");
                System.out.println("=========================");

                System.out.print(">> ");
                option = sc.next().charAt(0);
            }
            if (option == 'B' || option == 'b')
            {
                System.out.println("How many to deposit: ");
                cash = sc.nextInt();
                if (cash > 0)
                {
                    balance = balance + cash;
                    money = cash;

                    System.out.println("Deposit Succeed");
                    System.out.println("\n");
                }
                else
                {
                    System.out.println("Amount Not Valid!");
                    System.out.println("\n");
                }

                System.out.println("===================");
                System.out.println("Enter an option");
                System.out.println("===================");
                System.out.println("A. Check Balance");
                System.out.println("B. Deposit");
                System.out.println("C. Withdraw");
                System.out.println("D.Previous Activity");
                System.out.println("E. Exit");
                System.out.println("===================");

                System.out.print(">> ");
                option = sc.next().charAt(0);
            }
            if (option == 'C' || option == 'c')
            {
                System.out.println("How many to withdraw: ");
                cash = sc.nextInt();
                if (cash > 0 && balance>=cash)
                {
                    balance = balance - cash;
                    money = cash;

                    System.out.println("Withdrawal Succeed");
                    System.out.println("\n");
                }
                else
                {
                    System.out.println("Amount Not Valid!");
                    System.out.println("\n");
                }

                System.out.println("===================");
                System.out.println("Enter an option");
                System.out.println("===================");
                System.out.println("A. Check Balance");
                System.out.println("B. Deposit");
                System.out.println("C. Withdraw");
                System.out.println("D.Previous Activity");
                System.out.println("E. Exit");
                System.out.println("===================");

                System.out.print(">> ");
                option = sc.next().charAt(0);
            }
            if (option == 'D' || option == 'd')
            {
                System.out.println("Thanks For Using Our Services");
                break;
            }
            else
            {
                System.out.println("Command Not Found");
                System.out.println("===================");
                System.out.println("Enter an option");
                System.out.println("===================");
                System.out.println("A. Check Balance");
                System.out.println("B. Deposit");
                System.out.println("C. Withdraw");
                System.out.println("D.Previous Activity");
                System.out.println("E. Exit");
                System.out.println("===================");

                System.out.print(">> ");
                option = sc.next().charAt(0);
            }
        }
    }
}