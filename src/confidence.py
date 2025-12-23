def compute_overall_confidence(bureau_parameters, gst_sales):
    scores = []

    for param in bureau_parameters.values():
        if param["confidence"] > 0:
            scores.append(param["confidence"])

    for sale in gst_sales:
        if sale["confidence"] > 0:
            scores.append(sale["confidence"])

    if not scores:
        return 0.0

    return round(sum(scores) / len(scores), 2)
