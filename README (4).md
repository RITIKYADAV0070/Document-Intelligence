# 📄 Document Intelligence  
### AI-Powered Financial Document Understanding & Structured Data Extraction

---

## 🧠 Overview

**Document Intelligence** is an AI-driven system designed to **understand, extract, validate, and explain structured financial data** from complex, unstructured PDF documents such as:

- **CRIF Credit Bureau Reports**
- **GST GSTR-3B Returns**

The project demonstrates a **production-oriented approach** to document understanding by combining intelligent PDF parsing, semantic embeddings, and schema-aligned extraction to generate **clean, explainable JSON outputs** suitable for financial analytics, underwriting, compliance, and decision-making workflows.

---

## 🎯 Problem Statement

Financial documents pose persistent challenges:

- Highly inconsistent layouts across issuers  
- Tables interleaved with free-form text  
- Critical values scattered across multiple pages  
- Frequent format and structure changes  

### Limitations of Traditional Approaches
- Rule-based parsers break when layouts change  
- OCR-only systems lack semantic context  
- Manual extraction is slow, costly, and error-prone  

---

## ✅ Solution Summary

This project implements an **AI-first document intelligence pipeline** that:

- Locates information **semantically**, not positionally  
- Extracts financial values reliably across document formats  
- Maps outputs to a predefined schema  
- Provides **clear traceability** for every extracted field  

The system is designed as an **API-first backend**, enabling easy evaluation and integration.

---

## 🚀 Core Capabilities

### 1️⃣ CRIF Bureau Report Extraction
- Extracts predefined credit parameters as defined in the Excel schema  
- Identifies bureau score, account summaries, balances, delinquency indicators, and defaults  
- Produces structured JSON output  
- Includes page-level and section-level source references  

---

### 2️⃣ GSTR-3B GST Return Processing
- Parses monthly GSTR-3B PDFs  
- Extracts outward taxable supplies (Table 3.1(a))  
- Generates a monthly sales timeline

```json
[
  { "month": "2024-01", "sales": 1250000 },
  { "month": "2024-02", "sales": 1420000 }
]
```

---

### 3️⃣ Explainable & Auditable Outputs
Each extracted field includes:
- Extracted value  
- Source document reference (page / section)  
- Confidence score derived from semantic similarity  

This ensures auditability, regulator safety, and ease of debugging.

---

## 🧠 System Architecture

```
PDF Document
     ↓
PDF Parsing & Layout Understanding
     ↓
Page-Aware Intelligent Chunking
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
- Preservation of page-level metadata  

### Intelligent Chunking
- Logical, context-preserving segmentation  
- Avoids naïve fixed-length splits  

### Embeddings & Semantic Retrieval
- Embedding generation for:
  - Document chunks  
  - Parameter definitions  
- Similarity-based retrieval to locate relevant sections  
- Robust to layout and formatting variations  

### Extraction & Validation
- Schema-first extraction logic  
- Numeric normalization and validation  
- Deterministic, reproducible outputs  

---

## 📁 Project Structure

```
Document-Intelligence/
│
├── src/                     # Core extraction logic
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
├── ui/                      # Optional local UI (non-mandatory)
│
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 📊 Evaluation & Testing

### Evaluation Objectives
- Numerical accuracy of extracted fields  
- Schema completeness  
- Robustness across multi-page documents  
- Explainability and traceability  

### Evaluation Artifacts
All evaluation configurations and results are stored in:

```
evaluation/evaluation_report.json
```

This enables repeatable testing, transparent scoring, and regression analysis.

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

### Run API Locally
```bash
uvicorn src.api:app --reload
```

### Trigger Extraction
```http
POST /extract
```

- Executes the complete extraction pipeline  
- Returns structured, explainable JSON  
- Sufficient for full project evaluation  

---

## 🖥 Optional UI (Local Only)

A lightweight UI is included **only for local visualization**.

> The UI is **not required** for evaluation and does not affect extraction logic or accuracy.

The project is intentionally **API-first**, as per assignment requirements.

---

## 🛡️ Engineering Principles

- Explainability over black-box extraction  
- Schema-driven design  
- Deterministic and reproducible outputs  
- Clear separation of concerns  
- Production-oriented architecture  

---

## 🔐 Security & Compliance Notes

- No hard-coded secrets  
- Local-only document processing  
- Architecture supports easy extension for:
  - Encryption  
  - Access control  
  - Audit logging  

---

## 📌 Future Enhancements

- OCR support for fully scanned PDFs  
- Advanced table structure detection  
- Model fine-tuning for financial documents  
- Role-based access control  
- Scalable deployment pipelines  

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
