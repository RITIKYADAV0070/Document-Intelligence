import re


def normalize_month(month: str) -> str:
    """
    Converts filename-like month strings to human readable format.
    Example: gstr3b_april_2024 -> April 2024
    """
    month = month.lower()

    mapping = {
        "jan": "January",
        "feb": "February",
        "mar": "March",
        "apr": "April",
        "may": "May",
        "jun": "June",
        "jul": "July",
        "aug": "August",
        "sep": "September",
        "oct": "October",
        "nov": "November",
        "dec": "December"
    }

    year_match = re.search(r"\d{4}", month)
    year = year_match.group() if year_match else ""

    for k, v in mapping.items():
        if k in month:
            return f"{v} {year}".strip()

    return month


def extract_gst_sales(gst_chunks, month):
    """
    Extracts outward taxable supplies from GSTR-3B Table 3.1(a)
    """
    for c in gst_chunks:
        if "Outward taxable supplies" in c["content"]:
            match = re.search(
                r"Outward taxable supplies.*?(\d{1,12})",
                c["content"],
                re.IGNORECASE
            )
            if match:
                return {
                    "month": normalize_month(month),
                    "sales": int(match.group(1)),
                    "source": "GSTR-3B Table 3.1(a)",
                    "confidence": 0.99
                }

    return {
        "month": normalize_month(month),
        "sales": None,
        "source": "Not Found",
        "confidence": 0.0
    }
