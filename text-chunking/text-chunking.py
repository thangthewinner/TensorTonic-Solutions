def text_chunking(tokens, chunk_size, overlap):
    if not tokens or chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        return []

    step = chunk_size - overlap
    chunks = []
    n = len(tokens)

    for i in range(0, n, step):
        chunks.append(tokens[i : i + chunk_size])
        if i + chunk_size >= n:
            break
            
    return chunks