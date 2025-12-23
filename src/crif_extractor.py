import pandas as pd
import re
from src.embeddings import embed_texts, most_similar


def clean_number(text):
    """
    Extracts a reasonable numeric value from text.
    """
    if text is None:
        return None

    text = text.replace(",", "").strip()
    match = re.search(r"\b\d{1,9}\b", text)
    return int(match.group()) if match else None


def extract_boolean(text):
    """
    Extracts boolean values from CRIF text.
    """
    if text is None:
        return None

    text = text.lower()
    if "yes" in text or "default" in text:
        return True
    if "no" in text or "0" in text:
        return False
    return None


def validate_number(parameter_key, value):
    """
    Parameter-level numeric validation.
    Prevents false positives from IDs / reference numbers.
    """
    if value is None:
        return None

    # Bureau score must be between 300 and 900
    if parameter_key == "bureau_score":
        return value if 300 <= value <= 900 else None

    return value


def extract_crif_parameters(chunks, parameter_csv_path):
    """
    chunks: list of {page, content}
    returns: dict of extracted CRIF parameters
    """

    df = pd.read_csv(parameter_csv_path)

    # Build semantic queries from CSV
    queries = (
        df["parameter_name"]
        + " "
        + df["description"]
        + " "
        + df["expected_section"]
    ).tolist()

    query_embeddings = embed_texts(queries)
    chunk_embeddings = embed_texts([c["content"] for c in chunks])

    results = {}

    for idx, row in df.iterrows():
        best_chunk, similarity = most_similar(
            query_embeddings[idx],
            chunk_embeddings,
            chunks
        )

        text = best_chunk["content"]
        dtype = row["data_type"]
        param_key = row["parameter_key"]

        value = None

        if dtype == "number":
            raw_value = clean_number(text)
            value = validate_number(param_key, raw_value)

        elif dtype == "boolean":
            value = extract_boolean(text)

        if value is None:
            results[param_key] = {
                "value": None,
                "source": "not_found",
                "confidence": 0.0
            }
        else:
            results[param_key] = {
                "value": value,
                "source": f"{row['expected_section']} (page {best_chunk['page']})",
                "confidence": round(float(similarity), 2)
            }

    return results
