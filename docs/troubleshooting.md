# Troubleshooting
- Import errors: activate the virtual environment and install requirements from repo root.
- PyTorch GPU unavailable: check the wheel against OS, Python, and CUDA; CPU-only may be expected.
- Model download fails: check size, disk, access, and license requirements.
- API validation error: inspect Pydantic's response details and request schema.
- Incorrect RAG answer: inspect parsing, chunking, filters, retrieval ranking, context, and generation separately.
