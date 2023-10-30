
import exceptions.FileInitException;
import toyshop.Toyshop;


public class Main {
    public static final int NUMBER_OF_LAUNCHES = 10;
    public static void main(String[] args) {

        Toyshop toyshop = new Toyshop();
        toyshop.put("2 конструктор");
        toyshop.put("2 робот");
        toyshop.put("6 кукла");
        toyshop.put("1 машинка");
        System.out.println(toyshop.getInfo());

        toyshop.fileInit();
        int count = 0;
        for (int i = 0; i < NUMBER_OF_LAUNCHES; i++) {
            int winner = toyshop.get();
            String message = String.format("Победитель #%d:\t%s\n",
                    i + 1, toyshop.findToyByID(winner).getName());
            System.out.printf(message);
            try {
                toyshop.writeInFile(message);
                count++;
            } catch (FileInitException e) {
                System.out.println(e.getMessage());
            }
            if (count == NUMBER_OF_LAUNCHES) {
                System.out.println("\nЗапись в файл прошла успешно!");
            }
        }
    }
}