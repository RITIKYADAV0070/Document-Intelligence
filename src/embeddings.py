from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts, convert_to_tensor=True)

def most_similar(query_embedding, doc_embeddings, chunks):
    sims = cosine_similarity(
        query_embedding.unsqueeze(0),
        doc_embeddings
    )[0]

    idx = sims.argmax()
    return chunks[idx], float(sims[idx])
