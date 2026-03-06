package processors;

import model.Document;

public class TaxProcessor implements DocumentProcessor {

    public void process(Document document) {
        System.out.println("Procesando declaración tributaria: " + document.getName());
    }
}