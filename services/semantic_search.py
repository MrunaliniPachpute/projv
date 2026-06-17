import pickle

from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(
    MODEL_NAME
)

class SemanticSearch:

    def __init__(self):

        with open(
            "cache/embeddings.pkl",
            "rb"
        ) as f:

            data = pickle.load(f)

        self.embeddings = data[
            "embeddings"
        ]

        self.kb = data["kb"]

    def search(
        self,
        subject,
        description,
        top_k=3
    ):

        query = (
            subject + " " + description
        )

        query_emb = model.encode(
            [query]
        )

        scores = cosine_similarity(
            query_emb,
            self.embeddings
        )[0]

        result_df = self.kb.copy()

        result_df["score"] = scores

        return (
            result_df
            .sort_values(
                "score",
                ascending=False
            )
            .head(top_k)
        )