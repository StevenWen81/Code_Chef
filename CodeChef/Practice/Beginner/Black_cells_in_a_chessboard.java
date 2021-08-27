import java.util.Scanner;

class Black_cells_in_a_chessboard {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        System.out.println(number*number/2);
        input.close();
    }
}