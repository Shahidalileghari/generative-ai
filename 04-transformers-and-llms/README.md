# Transformers and LLM internals
Scaled dot-product attention:
Attention(Q,K,V) = softmax((QK^T / sqrt(d_k)) + M)V
where M is a mask; causal masks block future positions. Study multi-head attention, residual connections, normalization, feed-forward blocks, positional methods, decoding, temperature, top-k/top-p, context windows, and KV caches. Exact architecture details vary by model family.
