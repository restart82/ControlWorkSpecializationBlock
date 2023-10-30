package toys;

public class Toy implements ToyItem {
    private int id;
    private int weight;
    private String name;
    public Toy (int id, int weight, String name) {
        this.id = id;
        this.weight = weight;
        this.name = name;
    }

    public int getID() {
        return id;
    }

    public int getWeight() {
        return weight;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return  "ID" +
                id +
                ":\tИгрушка -\t\t" +
                name +
                "\n\t\tВес выпадания -\t" +
                weight +
                "\n\n";
    }

}
