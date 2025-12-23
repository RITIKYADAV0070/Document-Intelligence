# 📄 Document Intelligence
### AI-Powered Financial Document Understanding & Structured Data Extraction

---

## 🧠 Overview

**Document Intelligence** is an AI-driven backend system designed to **understand, extract, validate, and explain structured financial data** from complex, unstructured PDF documents such as:

- **CRIF Credit Bureau Reports**
- **GST GSTR-3B Returns**

This project is built **strictly according to the AI Assignment-2 specification** and focuses on **document understanding, financial data extraction, and structured, explainable JSON output**.

The system converts raw PDFs into **schema-aligned, auditable JSON** using intelligent parsing, semantic embeddings, and similarity-based retrieval.

---

## 🎯 Assignment Objectives — Fully Covered

✔ Parse CRIF Bureau Reports (PDF)  
✔ Extract credit parameters defined in Excel / CSV  
✔ Parse GSTR-3B Returns (PDF)  
✔ Generate monthly sales timeline  
✔ Structured JSON output with source & confidence  
✔ Semantic embeddings + cosine similarity  
✔ API / script-based execution  
✔ Explainability & traceability  
✔ Evaluation & confidence scoring  

---

## 📥 Input Documents

### CRIF Bureau Report (PDF)
Contains credit score, account summary, delinquency, balances, DPD, defaults, etc.

### GSTR-3B Return (PDF)
Contains outward taxable supplies and monthly GST sales.

### Parameter Definition Sheet (CSV / Excel)
Defines the exact CRIF parameters to extract.

> The pipeline is robust to layout variations and multi-page documents.

---

## 📤 Output Schema

```json
{
  "bureau_parameters": {
    "<parameter_key>": {
      "value": <number | boolean | null>,
      "source": "<document section / page>",
      "confidence": 0.0
    }
  },
  "gst_sales": [
    {
      "month": "April 2024",
      "sales": 976171,
      "source": "GSTR-3B Table 3.1(a)",
      "confidence": 0.99
    }
  ],
  "overall_confidence_score": 0.68
}
```

- **value** → extracted value  
- **source** → document section & page  
- **confidence** → similarity-based confidence score  

---

## 🧠 How It Works (High Level)

```
PDF Document
     ↓
PDF Parsing & Layout Understanding
     ↓
Page-Aware Intelligent Chunking
     ↓
Semantic Embeddings
     ↓
Similarity-Based Section Retrieval
     ↓
Targeted Field Extraction
     ↓
Schema Validation
     ↓
Explainable JSON Output
```

---

## ⚙️ Running Locally

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start API
```bash
python -m uvicorn src.api:app --reload
```

### Trigger Extraction
```http
POST http://127.0.0.1:8000/extract
```

- Executes full extraction pipeline  
- Saves output to `outputs/final_output.json`  
- Returns JSON response for evaluation  

---

## 📊 Evaluation & Testing

Evaluation artifacts are stored in:

```
evaluation/evaluation_report.json
```

Evaluation includes:
- Per-parameter accuracy  
- Confidence consistency  
- Overall confidence score  

This enables **repeatable testing and transparent evaluation**, as required by the assignment.

---

## 📁 Project Structure

```
Document-Intelligence/
│
├── src/                     # Core extraction logic
│   ├── loader.py
│   ├── chunker.py
│   ├── crif_extractor.py
│   ├── gstr_extractor.py
│   ├── embeddings.py
│   ├── confidence.py
│   └── api.py
│
├── data/                    # Input PDFs & parameter CSV
├── outputs/                 # Extracted JSON outputs
├── evaluation/              # Evaluation reports
├── ui/                      # Optional local UI (non-mandatory)
├── requirements.txt
└── README.md
```

---

## 🖥 Optional UI (Local Only)

A lightweight UI is included **only for local visualization**.

- UI is **not required** for assignment evaluation  
- Does **not affect** extraction logic or accuracy  

The project is intentionally **API-first**, exactly as specified.

---

## 🛡️ Engineering Principles

- Explainability over black-box extraction  
- Schema-driven design  
- Deterministic and reproducible outputs  
- Clean separation of concerns  
- Production-oriented thinking  

---

## 👤 Author

**Ritik Yadav**  
Software Engineer | AI & Document Intelligence  

- GitHub: https://github.com/RITIKYADAV0070  
- LinkedIn: https://www.linkedin.com/in/ritik-yadav-a43167232/

---

## 📄 License

This project is intended for **educational, evaluation, and internal review purposes only**.
