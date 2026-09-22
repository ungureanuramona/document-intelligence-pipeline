import streamlit as st

from extractor import extract_invoice_data


st.set_page_config(
    page_title="Document Intelligence Pipeline",
    page_icon="📄",
)

st.title("📄 Document Intelligence Pipeline")
st.write(
    "Upload a fictional invoice and extract validated structured data with a local LLM."
)

uploaded_file = st.file_uploader(
    "Upload a fictional invoice (.txt)",
    type=["txt"],
)

if uploaded_file is not None:
    document_text = uploaded_file.getvalue().decode("utf-8")

    st.subheader("Document preview")
    st.text(document_text)

    if st.button("Extract invoice data"):
        with st.spinner("Extracting and validating structured data..."):
            invoice_data = extract_invoice_data(document_text)

        st.subheader("Extracted JSON")
        st.json(invoice_data.model_dump())

        st.subheader("Key fields")
        first_column, second_column = st.columns(2)

        with first_column:
            st.metric("Invoice number", invoice_data.invoice_number)
            st.metric("Supplier", invoice_data.supplier_name)
            st.metric("Total amount", f"{invoice_data.total_amount:.2f} {invoice_data.currency}")

        with second_column:
            st.metric("Invoice date", invoice_data.invoice_date)
            st.metric("Customer", invoice_data.customer_name)
            st.metric("Payment terms", invoice_data.payment_terms)
else:
    st.info("Upload a fictional .txt invoice to begin.")