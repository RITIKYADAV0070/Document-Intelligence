# 📄 Document Intelligence  
### AI-Powered Financial Document Understanding & Structured Data Extraction

---

## 🧠 Overview

**Document Intelligence** is an AI-driven backend system designed to **understand, extract, validate, and explain structured financial data** from complex, unstructured PDF documents, specifically:

- **CRIF Credit Bureau Reports**
- **GST GSTR-3B Returns**

The project demonstrates a **production-oriented approach to document intelligence**, combining intelligent PDF parsing, semantic embeddings, and schema-driven extraction to produce **clean, explainable JSON outputs** suitable for financial analytics, underwriting, compliance, and automated decision-making workflows.

This implementation directly addresses the goals of **AI Assignment-2**, focusing on **document understanding, financial data extraction, and structured output generation**.

---

## 🎯 Problem Statement

Financial documents present persistent challenges:

- Inconsistent layouts across issuers  
- Tables interleaved with free-form text  
- Key values scattered across multiple pages  
- Frequent structural and formatting changes  

### Why Traditional Approaches Fail
- Rule-based parsers break with layout drift  
- OCR-only systems lack semantic context  
- Manual extraction is slow, costly, and error-prone  

---

## ✅ Solution Summary

This project implements an **AI-first document intelligence pipeline** that:

- Locates information **semantically**, not positionally  
- Extracts values reliably across document variations  
- Maps outputs to a predefined extraction schema  
- Provides **clear traceability and confidence** for every field  

The system is designed as an **API-first backend**, enabling easy evaluation, reproducibility, and future integration.

---

## 🚀 Core Capabilities

### 1️⃣ CRIF Bureau Report Extraction
- Extracts all credit parameters defined in the provided Excel sheet  
- Includes bureau score, account counts, balances, delinquency indicators, and defaults  
- Handles multi-page tables and repeated sections  
- Produces structured, schema-aligned JSON  
- Includes **page-level and section-level source references**

---

### 2️⃣ GSTR-3B GST Return Processing
- Parses monthly GSTR-3B PDFs  
- Extracts **Outward Taxable Supplies** from **Table 3.1(a)**  
- Generates a monthly sales timeline

```json
[
  { "month": "April 2024", "sales": 976171 },
  { "month": "May 2024", "sales": 1023340 }
]
```

---

### 3️⃣ Explainable & Auditable Outputs
Each extracted field includes:
- Extracted value  
- Source document section (with page reference)  
- Confidence score derived from semantic similarity  

This ensures **auditability, regulator safety, and easy debugging**.

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

## 📁 Project Structure

```
Document-Intelligence/
│
├── data/
│   ├── crif_reports/
│   ├── gstr3b_reports/
│   └── parameters.csv
│
├── src/
│
├── outputs/
│   └── final_output.json
│
├── evaluation/
│   └── evaluation_report.json
│
├── tests/
│   └── evaluate.py
│
├── requirements.txt
└── README.md
```

---

## 📊 Evaluation & Testing

Evaluation results are stored in:

```
evaluation/evaluation_report.json
```

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/RITIKYADAV0070/Document-Intelligence.git
cd Document-Intelligence
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
uvicorn src.api:app --reload
```

```http
POST /extract
```

---

## 🖥 Optional Local UI

A lightweight UI exists **only for local visualization** and is **not required for evaluation**.

---

## 👤 Author

**Ritik Yadav**  
Software Engineer | AI & Document Intelligence  
