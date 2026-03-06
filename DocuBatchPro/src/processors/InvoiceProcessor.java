package processors;

import model.Document;

public class InvoiceProcessor implements DocumentProcessor {

    public void process(Document document) {
        System.out.println("Procesando factura: " + document.getName());
    }
}