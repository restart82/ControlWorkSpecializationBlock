package toyshop;

public interface Lottery {
    /**
    * Метод добавляет элемент типа Toy в коллекцию PriorityQueue
     */
    void put(String string);

    /**
    * Метод возвращает ID победителя розыгрыша
     */
    int get();
}
