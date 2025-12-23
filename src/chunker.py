def chunk_document(pages):
    chunks = []
    for page in pages:
        chunks.append({
            "page": page["page"],
            "content": page["content"]
        })
    return chunks
