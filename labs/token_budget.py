"""Character-based teaching approximation, not a real tokenizer."""
def estimate_tokens(text: str, chars_per_token: float = 4.0) -> int:
    if chars_per_token <= 0:
        raise ValueError("chars_per_token must be positive")
    return round(len(text) / chars_per_token)

if __name__ == "__main__":
    sample = "A language model predicts the next token from prior context."
    print("Rough token estimate:", estimate_tokens(sample))
    print("Use the actual model tokenizer for real budgets.")
