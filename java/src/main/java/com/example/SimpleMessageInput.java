package src.main.java.com.example;
import java.util.Scanner;

public class SimpleMessageInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String message = "";
        String displayedMessage = "";

        while (true) {
            System.out.println("\n--- Simple Message Input ---");
            System.out.println("Escribe tu mensaje (o 'salir' para terminar):");
            message = scanner.nextLine();

            if (message.equalsIgnoreCase("salir")) {
                break;
            }

            displayedMessage = message;
            System.out.println("\nMensaje enviado: " + displayedMessage);
        }

        scanner.close();
        System.out.println("Programa terminado.");
    }
}
