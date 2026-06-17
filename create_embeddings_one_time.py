import os
import pickle

from sentence_transformers import SentenceTransformer

from services.data_loader import (
    load_complaints,
    load_acknowledgements
)

from services.knowledge_base import (
    build_closed_ticket_kb
)

MODEL_NAME = "all-MiniLM-L6-v2"

print("Loading data...")

complaints = load_complaints()
acks = load_acknowledgements()

print("Building knowledge base...")

kb = build_closed_ticket_kb(
    complaints,
    acks
)

print(f"Closed tickets found: {len(kb)}")

texts = (
    kb["subject"].fillna("")
    + " "
    + kb["complaint"].fillna("")
)

print("Loading embedding model...")

model = SentenceTransformer(
    MODEL_NAME
)

print("Generating embeddings...")

embeddings = model.encode(
    texts.tolist(),
    show_progress_bar=True
)

os.makedirs(
    "cache",
    exist_ok=True
)

with open(
    "cache/embeddings.pkl",
    "wb"
) as f:

    pickle.dump(
        {
            "embeddings": embeddings,
            "kb": kb
        },
        f
    )

print("Done!")
print(
    "Saved -> cache/embeddings.pkl"
)