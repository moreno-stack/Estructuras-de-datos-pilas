package processors;

import model.Document;

public class ReportProcessor implements DocumentProcessor {

    public void process(Document document) {
        System.out.println("Procesando reporte financiero: " + document.getName());
    }
}