package factory;

import processors.*;

public class DocumentFactory {

    public static DocumentProcessor createProcessor(String type) {

        switch (type.toLowerCase()) {

            case "factura":
                return new InvoiceProcessor();

            case "contrato":
                return new ContractProcessor();

            case "reporte":
                return new ReportProcessor();

            case "certificado":
                return new CertificateProcessor();

            case "declaracion":
                return new TaxProcessor();

            default:
                throw new IllegalArgumentException("Tipo de documento no soportado");
        }
    }
}