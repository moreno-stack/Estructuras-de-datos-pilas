package main;

import model.Document;
import service.BatchProcessor;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        List<Document> documents = new ArrayList<>();

        documents.add(new Document("Factura001.pdf","factura","Colombia"));
        documents.add(new Document("ContratoA.docx","contrato","Mexico"));
        documents.add(new Document("Reporte2025.xlsx","reporte","Chile"));
        documents.add(new Document("CertificadoDigital.pdf","certificado","Argentina"));
        documents.add(new Document("DeclaracionRenta.csv","declaracion","Colombia"));

        BatchProcessor batch = new BatchProcessor();

        batch.processBatch(documents);

    }
}