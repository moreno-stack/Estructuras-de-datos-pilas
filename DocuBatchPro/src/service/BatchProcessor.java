package service;

import factory.DocumentFactory;
import model.Document;
import processors.DocumentProcessor;

import java.util.List;

public class BatchProcessor {

    public void processBatch(List<Document> documents) {

        for (Document doc : documents) {

            DocumentProcessor processor =
                    DocumentFactory.createProcessor(doc.getType());

            processor.process(doc);

        }
    }
}