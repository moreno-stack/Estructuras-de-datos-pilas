package processors;

import model.Document;

public class ContractProcessor implements DocumentProcessor {

    public void process(Document document) {
        System.out.println("Procesando contrato: " + document.getName());
    }
}