from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# ==========================================
# MODEL
# ==========================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []
sources = []

# ==========================================
# CHUNKING
# ==========================================

def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks


# ==========================================
# LOAD DOCUMENTS
# ==========================================

def load_documents():

    global documents
    global sources

    documents.clear()
    sources.clear()

    knowledge_path = "knowledge"

    for root, dirs, files in os.walk(
        knowledge_path
    ):

        for file in files:

            if file.endswith(".md"):

                file_path = os.path.join(
                    root,
                    file
                )

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                    chunks = chunk_text(
                        content
                    )

                    for chunk in chunks:

                        documents.append(
                            chunk
                        )

                        sources.append(
                            file_path
                        )


# ==========================================
# BUILD FAISS INDEX
# ==========================================

def build_index():

    load_documents()

    if len(documents) == 0:

        raise ValueError(
            "No knowledge documents found."
        )

    embeddings = model.encode(
        documents
    )

    embeddings = np.array(
        embeddings
    ).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    return index


# ==========================================
# INITIALIZE INDEX
# ==========================================

index = build_index()


# ==========================================
# SEARCH KNOWLEDGE
# ==========================================

def search_knowledge(
    query,
    top_k=1
):

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):

            results.append(
                f"""
Source:
{sources[idx]}

Content:
{documents[idx]}
"""
            )

    return "\n\n".join(results)