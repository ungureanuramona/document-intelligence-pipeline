import csv
from io import StringIO

import streamlit as st

from extractor import extract_invoice_data, read_document


def create_csv(results):
    output = StringIO()

    writer = csv.DictWriter(
        output,
        fieldnames=results[0].keys(),
    )
    writer.writeheader()
    writer.writerows(results)

    return output.getvalue()


st.set_page_config(
    page_title="Document Intelligence Pipeline",
    page_icon="📄",
)

st.title("📄 Document Intelligence Pipeline")
st.write(
    "Upload fictional invoice documents and extract validated structured data with a local LLM."
)

uploaded_files = st.file_uploader(
    "Upload fictional invoices",
    type=["txt", "pdf"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.write(f"Selected documents: {len(uploaded_files)}")

    if st.button("Extract invoice data"):
        results = []

        with st.spinner("Extracting and validating structured data..."):
            for uploaded_file in uploaded_files:
                try:
                    document_text = read_document(
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                    )

                    invoice_data = extract_invoice_data(document_text)

                    result = invoice_data.model_dump()
                    result["source_file"] = uploaded_file.name
                    results.append(result)

                except Exception as error:
                    st.error(
                        f"Could not process {uploaded_file.name}: {error}"
                    )

        if results:
            st.subheader("Extracted invoice data")
            st.dataframe(results, use_container_width=True)

            csv_data = create_csv(results)

            st.download_button(
                label="Download all results as CSV",
                data=csv_data,
                file_name="extracted_invoices.csv",
                mime="text/csv",
            )

            st.subheader("Individual JSON results")

            for result in results:
                with st.expander(result["source_file"]):
                    st.json(result)
else:
    st.info("Upload one or more fictional .txt or .pdf invoices to begin.")