from fastapi import FastAPI
from examples.api.schemas import GenerateRequest, GenerateResponse

app = FastAPI(title="Generative AI Mastery Demo API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate-demo", response_model=GenerateResponse)
def generate_demo(request: GenerateRequest):
    # Deterministic mock only; no LLM/provider call is made.
    prompt = request.prompt.strip()
    return GenerateResponse(
        output=f"Demo received your prompt ({len(prompt)} characters). "
               "Connect a model provider behind this server-side boundary.",
        model="deterministic-demo",
    )
