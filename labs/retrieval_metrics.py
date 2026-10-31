def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not relevant:
        return 0.0
    return len(set(retrieved[:k]) & relevant) / len(relevant)

def reciprocal_rank(retrieved: list[str], relevant: set[str]) -> float:
    for rank, doc_id in enumerate(retrieved, start=1):
        if doc_id in relevant:
            return 1.0 / rank
    return 0.0

if __name__ == "__main__":
    ranking, expected = ["doc-7", "doc-2", "doc-9", "doc-1"], {"doc-2", "doc-1"}
    print("Recall@3:", recall_at_k(ranking, expected, 3))
    print("Reciprocal rank:", reciprocal_rank(ranking, expected))
