# 📄 Document Intelligence  
### AI-Powered Financial Document Understanding & Data Extraction

---

## 🔥 TL;DR (For Evaluators & Reviewers)

- Extracts structured financial data from unstructured PDFs  
- Supports CRIF Credit Bureau Reports and GST GSTR-3B Returns  
- Uses semantic embeddings for robust information retrieval  
- Produces explainable, auditable JSON outputs  
- Designed for accuracy, robustness, and production readiness  

---

## 🧠 Executive Summary

**Document Intelligence** is a production-ready AI system designed to **understand, extract, validate, and explain structured financial data from complex, unstructured PDF documents**, including:

- CRIF Credit Bureau Reports  
- GST GSTR-3B Returns  

The system converts raw PDFs into **schema-aligned, explainable JSON outputs** using:

- Intelligent PDF parsing  
- Semantic embeddings & retrieval  
- Targeted extraction pipelines  
- Structured evaluation and validation  

This solution is suitable for **financial analytics, compliance, underwriting, and decisioning workflows**.

---

## 🎯 Problem Statement

Financial documents present several challenges:

- Inconsistent layouts across issuers  
- Tables mixed with unstructured text  
- Critical values scattered across pages  
- Frequent format changes  

### Why Traditional Approaches Fail
- Rule-based parsing breaks with layout changes  
- OCR-only systems lack semantic understanding  
- Manual extraction is slow, costly, and error-prone  

---

## ✅ Solution Overview

An AI-first document intelligence pipeline that:

- Locates information semantically (not position-based)  
- Extracts values reliably across document formats  
- Maps outputs to predefined schemas  
- Explains where and why each value was extracted  

---

## 🚀 Key Capabilities

### 1️⃣ CRIF Bureau Report Extraction
- Extracts predefined credit parameters (as per Excel schema)  
- Identifies credit score, account summaries, outstanding balances, and payment behavior  
- Outputs structured JSON  
- Includes page / section-level source explanations  

---

### 2️⃣ GSTR-3B GST Return Processing
- Parses monthly GSTR-3B PDFs  
- Extracts outward supplies (sales)  
- Generates a monthly sales timeline:

```json
[
  { "month": "2024-01", "sales": 1250000 },
  { "month": "2024-02", "sales": 1420000 }
]
```

---

### 3️⃣ Explainable & Auditable Output
Each extracted field includes:
- Extracted value  
- Source document reference (page / section)  
- Extraction reasoning  
- Confidence (where applicable)  

This ensures auditability, regulator safety, and easy debugging.

---

## 🧠 System Architecture

```
PDF Document
     ↓
PDF Parsing & Layout Understanding
     ↓
Intelligent Chunking (Page-Aware)
     ↓
Semantic Embeddings
     ↓
Relevant Section Retrieval
     ↓
Targeted Field Extraction
     ↓
Schema Validation
     ↓
Explainable JSON Output
```

---

## 🏗️ Technical Design

### Document Ingestion
- Text and table extraction from PDFs  
- Page-level metadata preservation  

### Intelligent Chunking
- Logical segmentation instead of naive splitting  
- Context-preserving chunks  

### Embeddings & Semantic Search
- Converts chunks into embeddings  
- Uses similarity search to locate relevant sections  
- Robust to layout and formatting variations  

### Extraction & Validation
- Schema-first extraction  
- Field-level validation  
- Deterministic outputs  

---

## 📁 Project Structure

```
Document-Intelligence/
│
├── src/                     # Core system logic
│   ├── loaders/             # PDF loaders & preprocessors
│   ├── extractors/          # CRIF & GST extraction pipelines
│   ├── embeddings/          # Embedding generation & retrieval
│   ├── validators/          # Schema & consistency checks
│   └── utils/               # Helper utilities
│
├── data/                    # Sample input PDFs
│
├── evaluation/              # Evaluation configs & reports
│   └── evaluation_report.json
│
├── outputs/                 # Final structured JSON outputs
│
├── tests/                   # Unit & integration tests
│
├── ui/                      # Optional UI / API layer
│
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 📊 Evaluation & Testing

### Evaluation Goals
- Accuracy of extracted fields  
- Schema completeness  
- Robustness across document formats  
- Explainability and traceability  

### Evaluation Artifacts
All evaluation configurations and results are stored in:

```
evaluation/evaluation_report.json
```

This enables transparent scoring, repeatable testing, and regression safety.

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/RITIKYADAV0070/Document-Intelligence.git
cd Document-Intelligence
pip install -r requirements.txt
```

> Python 3.9+ recommended

---

## ▶️ Usage

### CRIF Extraction
```bash
python src/extractors/crif_extractor.py --input data/crif_report.pdf
```

### GST Sales Timeline
```bash
python src/extractors/gst_extractor.py --input data/gstr3b.pdf
```

### Output
- Saved in the `outputs/` directory  
- Fully structured and explainable JSON  

---

## 🛡️ Engineering Principles

- Explainability over black-box extraction  
- Schema-first design  
- Deterministic and reproducible outputs  
- Clear separation of concerns  
- Production-oriented architecture  

---

## 🔐 Security & Compliance Notes

- No hard-coded secrets  
- Local-only document processing  
- Easy extension for:
  - Encryption  
  - Access control  
  - Audit logging  

---

## 📌 Future Enhancements

- OCR support for scanned PDFs  
- FastAPI-based REST service  
- Interactive analytics dashboard  
- Fine-tuned financial document models  
- Role-based access control  

---

## 👤 Author

**Ritik Yadav**  
Software Engineer | AI & Document Intelligence  

- GitHub: https://github.com/RITIKYADAV0070  
- LinkedIn: https://www.linkedin.com/in/ritik-yadav-a43167232/

---

## 📄 License

This project is intended for **educational, evaluation, and internal review purposes**.  
Commercial usage requires prior authorization.
