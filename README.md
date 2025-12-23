# 📄 Document Intelligence  
### AI-Powered Financial Document Understanding & Data Extraction

---

## 🧠 Executive Summary

**Document Intelligence** is a production-ready AI system designed to **understand, extract, and explain structured financial data from complex, unstructured PDF documents** such as **CRIF Credit Bureau Reports** and **GST GSTR-3B Returns**.

The system converts raw PDFs into **auditable, explainable, schema-aligned JSON outputs** using intelligent PDF parsing, semantic embeddings, targeted extraction pipelines, and structured evaluation.

---

## 🎯 Problem Statement

Financial documents suffer from:
- Inconsistent layouts across issuers  
- Tables mixed with free-form text  
- Critical values spread across pages  

Rule-based parsing fails at scale, while manual processing is slow and error-prone.

### ✅ Solution
An AI-first document intelligence pipeline that:
- Locates relevant information semantically  
- Extracts values reliably  
- Maps them to predefined schemas  
- Explains *where and why* each value was extracted  

---

## 🚀 Key Capabilities

### CRIF Bureau Report Extraction
- Extracts predefined credit parameters  
- Identifies credit score, account summaries, outstanding balances, and payment behavior  
- Outputs structured JSON with page-level source explanations  

### GSTR-3B GST Return Processing
- Parses monthly GSTR-3B PDFs  
- Generates a monthly sales timeline  

```json
[
  { "month": "2024-01", "sales": 1250000 },
  { "month": "2024-02", "sales": 1420000 }
]
```

### Explainable Output
Each extracted field includes:
- Value  
- Document source (page / section)  
- Extraction reasoning  
- Confidence (where applicable)  

---

## 🧠 System Architecture

PDF → Parsing & Chunking → Embeddings → Semantic Retrieval → Structured Extraction → Explainable JSON

---

## 📁 Project Structure

```
Document-Intelligence/
├── src/
├── data/
├── evaluation/
│   └── evaluation_report.json
├── outputs/
├── tests/
├── ui/
├── requirements.txt
└── README.md
```

---

## 📊 Evaluation

Evaluation artifacts and metrics are stored in:

```
evaluation/evaluation_report.json
```

This ensures transparency, repeatability, and regression safety before production.

---

## ⚙️ Setup

```bash
git clone https://github.com/RITIKYADAV0070/Document-Intelligence.git
cd Document-Intelligence
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python src/extractors/crif_extractor.py
python src/extractors/gst_extractor.py
```

Outputs are saved in the `outputs/` directory with structured JSON and explanations.

---

## 🛡️ Engineering Principles

- Explainability over black-box extraction  
- Schema-first design  
- Deterministic outputs  
- Separation of concerns  
- Production-readiness  

---

## 📌 Future Enhancements

- OCR support for scanned PDFs  
- REST API using FastAPI  
- Analytics dashboard  
- Fine-tuned financial document models  
- Role-based access control  

---

## 👤 Author

**Ritik Yadav**  
GitHub: https://github.com/RITIKYADAV0070  
LinkedIn: https://www.linkedin.com/in/ritik-yadav-a43167232/

---

## 📄 License

This project is intended for **educational, evaluation, and internal review purposes**.
