package model;

public class Document {

    private String name;
    private String type;
    private String country;

    public Document(String name, String type, String country) {
        this.name = name;
        this.type = type;
        this.country = country;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public String getCountry() {
        return country;
    }
}