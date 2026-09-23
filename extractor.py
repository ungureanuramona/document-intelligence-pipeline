from io import BytesIO
from pathlib import Path

from ollama import chat
from pydantic import BaseModel
from pypdf import PdfReader


LLM_MODEL_NAME = "gemma3:4b"


class InvoiceData(BaseModel):
    invoice_number: str
    invoice_date: str
    supplier_name: str
    customer_name: str
    currency: str
    total_amount: float
    payment_terms: str


def read_document(file_name, file_content):
    file_extension = Path(file_name).suffix.lower()

    if file_extension == ".txt":
        return file_content.decode("utf-8")

    if file_extension == ".pdf":
        reader = PdfReader(BytesIO(file_content))

        return "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

    raise ValueError("Only .txt and .pdf files are supported.")


def extract_invoice_data(document_text):
    response = chat(
        model=LLM_MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You extract structured information from fictional invoices. "
                    "Use only information found in the document. "
                    "Return the requested JSON fields."
                ),
            },
            {
                "role": "user",
                "content": document_text,
            },
        ],
        format=InvoiceData.model_json_schema(),
        options={"temperature": 0},
    )

    return InvoiceData.model_validate_json(response.message.content)


def main():
    project_folder = Path(__file__).parent
    document_path = project_folder / "documents" / "sample_invoice.pdf"

    document_text = read_document(
        document_path.name,
        document_path.read_bytes(),
    )

    print("Extracting structured invoice data...\n")

    invoice_data = extract_invoice_data(document_text)

    print(invoice_data.model_dump_json(indent=2))


if __name__ == "__main__":
    main()