# Document Intelligence Pipeline

A local AI application that extracts validated structured data from fictional invoice documents.

## Features

- Uploads one or more fictional invoices in `.txt` and `.pdf` formats
- Extracts text from PDF files with `pypdf`
- Uses a local LLM with Ollama and Gemma 3
- Validates extracted data with Pydantic
- Displays extracted data in a Streamlit web interface
- Shows individual JSON results for each document
- Exports multiple extraction results to a CSV file
- Includes automated tests for document reading

## Extracted fields

- Invoice number
- Invoice date
- Supplier name
- Customer name
- Currency
- Total amount
- Payment terms
- Source file name

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

## Run tests

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

## Project structure

```text
document-intelligence-pipeline/
├── documents/
│   ├── sample_invoice.txt
│   └── sample_invoice.pdf
├── tests/
│   └── test_extractor.py
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
- unittest