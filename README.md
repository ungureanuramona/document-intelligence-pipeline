# Document Intelligence Pipeline

A local Python application that extracts validated structured data from fictional invoice documents.

The application uses a local LLM to turn unstructured invoice text into JSON, then validates the result with Pydantic.

## Features

- Uploads fictional invoice documents in `.txt` format
- Extracts invoice number, date, supplier, customer, currency, total amount, and payment terms
- Uses a local Ollama model (`gemma3:4b`)
- Validates extracted data with Pydantic
- Displays JSON and key fields in a Streamlit web interface
- Uses fictional sample documents only

## Example Output

```json
{
  "invoice_number": "INV-2026-1042",
  "invoice_date": "2026-09-21",
  "supplier_name": "Northwind Components Ltd.",
  "customer_name": "Contoso Retail SRL",
  "currency": "EUR",
  "total_amount": 3570.0,
  "payment_terms": "Net 30 days"
}
```

## Project Structure

```text
document-intelligence-pipeline/
├── documents/
│   └── sample_invoice.txt
├── app.py
├── extractor.py
└── requirements.txt
```

## Run Locally

### 1. Create and install the Python environment

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Start Ollama with Docker

Docker Desktop must be running.

```powershell
docker start ollama
```

If the container does not exist yet:

```powershell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### 3. Download the local model

```powershell
docker exec -it ollama ollama pull gemma3:4b
```

### 4. Run the web application

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open `http://localhost:8501` if the browser does not open automatically.

## Tech Stack

- Python
- Streamlit
- Pydantic
- Ollama
- Gemma 3 4B
- Docker
- Git and GitHub