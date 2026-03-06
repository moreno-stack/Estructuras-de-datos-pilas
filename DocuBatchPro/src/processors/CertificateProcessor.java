package processors;

import model.Document;

public class CertificateProcessor implements DocumentProcessor {

    public void process(Document document) {
        System.out.println("Procesando certificado digital: " + document.getName());
    }
}