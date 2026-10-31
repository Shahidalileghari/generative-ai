import pytest
from labs.token_budget import estimate_tokens
from labs.retrieval_metrics import recall_at_k, reciprocal_rank

def test_token_estimate():
    assert estimate_tokens("abcdefgh") == 2

def test_invalid_token_ratio():
    with pytest.raises(ValueError):
        estimate_tokens("text", 0)

def test_recall_at_k():
    assert recall_at_k(["a", "b", "c"], {"b", "d"}, 3) == 0.5

def test_reciprocal_rank():
    assert reciprocal_rank(["x", "b", "a"], {"a", "b"}) == 0.5
