# Document Intelligence Pipeline

A local AI application that extracts validated structured data from fictional invoice documents.

## Features

- Uploads fictional invoice documents in `.txt` and `.pdf` formats
- Extracts text from PDF files with `pypdf`
- Uses a local LLM with Ollama and Gemma 3
- Validates extracted data with Pydantic
- Displays structured JSON and key invoice fields in a Streamlit interface
- Includes a fictional sample invoice in TXT and PDF format

## Example extracted fields

- Invoice number
- Invoice date
- Supplier name
- Customer name
- Currency
- Total amount
- Payment terms

## Run locally

1. Start Docker Desktop.

2. Start the local Ollama container:

```powershell
docker start ollama
```

3. Run the Streamlit application:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

4. Open the local address shown in the terminal, usually:

```text
http://localhost:8501
```

## Project structure

```text
document-intelligence-pipeline/
├── documents/
│   ├── sample_invoice.txt
│   └── sample_invoice.pdf
├── app.py
├── create_sample_invoice_pdf.py
├── extractor.py
└── requirements.txt
```

## Tech stack

- Python
- Streamlit
- Ollama
- Gemma 3
- Pydantic
- pypdf
- ReportLab