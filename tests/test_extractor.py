import unittest
from pathlib import Path

from extractor import read_document


PROJECT_FOLDER = Path(__file__).resolve().parent.parent


class ReadDocumentTests(unittest.TestCase):
    def test_reads_text_file(self):
        document_text = read_document(
            "invoice.txt",
            b"Invoice Number: INV-001",
        )

        self.assertEqual(document_text, "Invoice Number: INV-001")

    def test_reads_pdf_file(self):
        pdf_path = PROJECT_FOLDER / "documents" / "sample_invoice.pdf"

        document_text = read_document(
            pdf_path.name,
            pdf_path.read_bytes(),
        )

        self.assertIn("Invoice Number: INV-2026-1042", document_text)
        self.assertIn("Total Amount: 3,570.00 EUR", document_text)

    def test_rejects_unsupported_file_type(self):
        with self.assertRaises(ValueError):
            read_document(
                "invoice.docx",
                b"This is not a supported file.",
            )


if __name__ == "__main__":
    unittest.main()