import os
import json
from src.loader import load_pdf
from src.chunker import chunk_document
from src.crif_extractor import extract_crif_parameters
from src.gstr_extractor import extract_gst_sales
from src.confidence import compute_overall_confidence



CRIF_DIR = "data/crif_reports"
GST_DIR = "data/gstr3b_reports"
PARAMETERS = "data/parameters.csv"
OUTPUT_PATH = "outputs/final_output.json"


def main():
    # ---------- CRIF ----------
    crif_files = [f for f in os.listdir(CRIF_DIR) if f.endswith(".pdf")]
    all_bureau_results = {}

    for pdf in crif_files:
        pages = load_pdf(os.path.join(CRIF_DIR, pdf))
        chunks = chunk_document(pages)
        bureau_data = extract_crif_parameters(chunks, PARAMETERS)
        all_bureau_results[pdf] = bureau_data

    # ---------- GST ----------
    gst_sales = []
    for pdf in os.listdir(GST_DIR):
        if pdf.endswith(".pdf"):
            month = pdf.replace(".pdf", "")
            pages = load_pdf(os.path.join(GST_DIR, pdf))
            chunks = chunk_document(pages)
            gst_sales.append(extract_gst_sales(chunks, month))

    overall_conf = compute_overall_confidence(
        list(all_bureau_results.values())[0],
        gst_sales
    )

    final_output = {
        "bureau_parameters": list(all_bureau_results.values())[0],
        "gst_sales": gst_sales,
        "overall_confidence_score": overall_conf
    }

    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(final_output, f, indent=2)

    print("✅ Extraction complete. Output written to outputs/final_output.json")


if __name__ == "__main__":
    main()
