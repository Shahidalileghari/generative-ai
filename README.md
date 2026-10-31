# Generative AI Mastery

An engineering-focused curriculum from AI foundations to production LLM applications.

**Stack:** Python 3.11+, PyTorch (optional for local labs), Hugging Face ecosystem, FastAPI, Pydantic, pytest. Verify current library/model documentation and licenses before use.

## Learning outcomes
- Understand ML foundations, neural networks, tokenization, embeddings, and transformers.
- Explain autoregressive generation, attention, decoding, and context windows.
- Build LLM applications with prompts, structured outputs, and reliable API boundaries.
- Implement retrieval-augmented generation (RAG), evaluation, and citations.
- Understand fine-tuning, LoRA/PEFT, tool calling, and bounded agents.
- Apply safety, security, privacy, deployment, observability, and cost controls.

## Curriculum
| Stage | Topics |
|---|---|
| 00 | Setup and roadmap |
| 01 | Probability, vectors, ML foundations |
| 02 | Neural networks and embeddings |
| 03 | NLP, tokenization, language modeling |
| 04 | Transformers, attention, LLM internals |
| 05 | Prompting, structured output, model APIs |
| 06 | RAG, vector search, reranking, grounding |
| 07 | Fine-tuning, instruction data, LoRA |
| 08 | Tool calling and agentic systems |
| 09 | Evaluation, safety, prompt injection, privacy |
| 10 | Deployment, observability, cost, resilience |
| 11 | Portfolio projects |

## Quick start
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest
uvicorn examples.api.main:app --reload
```
Open `http://127.0.0.1:8000/docs`. The included API is a deterministic mock; it does not call an LLM.

For PyTorch, install the correct wheel for your platform/accelerator using https://pytorch.org/get-started/locally/.

## Engineering principles
- Model output is not automatically factual or verified.
- Treat retrieved documents, user input, and tool output as untrusted data.
- Enforce authorization in backend code, never in prompts.
- Keep provider secrets server-side.
- Validate structured output before using it.
- Evaluate retrieval, generation, safety, latency, and cost independently.
- Bound tool permissions, execution time, steps, and spend.

## Limitations
No pretrained weights, paid API credentials, or trained model are included. Some labs require external services, datasets, or GPU resources. This is a learning curriculum, not a claim that a model has been trained.

MIT License. See `LICENSE`.
