
import exceptions.FileInitException;
import toyshop.Toyshop;


public class Main {
//    public static final int NUMBER_OF_LAUNCHES = 10;
    public static void main(String[] args) {

        Toyshop toyshop = new Toyshop();
        toyshop.put("2 конструктор");
        toyshop.put("2 робот");
        toyshop.put("6 кукла");
        toyshop.put("1 машинка");
        System.out.println(toyshop.getInfo());

        toyshop.changeWeight(1, 3);
        System.out.println(toyshop.getInfo());
        int numberOfLaunches = toyshop.getSize();

        toyshop.fileInit();
        int count = 0;
        for (int i = 0; i < numberOfLaunches; i++) {
            try {
                toyshop.get();
                count++;
            } catch (FileInitException e) {
                System.out.println(e.getMessage());
            }
            if (count == numberOfLaunches) {
                System.out.println("Запись прошла успешно!");
            }
        }
    }
}