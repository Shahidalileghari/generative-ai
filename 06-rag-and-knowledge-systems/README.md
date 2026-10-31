# RAG and knowledge systems
Pipeline: parse -> normalize -> chunk -> embed -> index -> retrieve -> filter/rerank -> assemble context -> generate -> validate/cite.
Evaluate retrieval (Recall@k, Precision@k, MRR/nDCG) separately from groundedness and answer quality. Preserve source metadata and enforce tenant authorization during retrieval. RAG does not guarantee correctness.
