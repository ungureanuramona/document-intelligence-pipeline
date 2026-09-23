from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def main():
    project_folder = Path(__file__).parent
    output_path = project_folder / "documents" / "sample_invoice.pdf"

    lines = [
        "Commercial Invoice",
        "",
        "Invoice Number: INV-2026-1042",
        "Invoice Date: 2026-09-21",
        "",
        "Supplier:",
        "Northwind Components Ltd.",
        "45 Industrial Road",
        "London, United Kingdom",
        "",
        "Customer:",
        "Contoso Retail SRL",
        "12 Business Avenue",
        "Bucharest, Romania",
        "",
        "Items:",
        "- Network controller units: 10 x 250.00 EUR",
        "- Installation service: 1 x 500.00 EUR",
        "",
        "Subtotal: 3,000.00 EUR",
        "VAT: 570.00 EUR",
        "Total Amount: 3,570.00 EUR",
        "",
        "Payment Terms: Net 30 days",
    ]

    pdf = canvas.Canvas(str(output_path), pagesize=A4)
    text = pdf.beginText(50, 800)
    text.setFont("Helvetica", 12)

    for line in lines:
        text.textLine(line)

    pdf.drawText(text)
    pdf.save()

    print(f"Created: {output_path.name}")


if __name__ == "__main__":
    main()