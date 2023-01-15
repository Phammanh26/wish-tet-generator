from fuzzywuzzy import fuzz

def get_text_scores(q_text, v_texts):
    q_text = q_text.replace('\n', ' ').lower()
    v_texts = [v_text.replace('\n', ' ').lower() for v_text in v_texts]
    scores = [fuzz.partial_ratio(q_text, v_text) for v_text in v_texts]
    return scores

def get_text_topk(q_text, v_texts, k=5):
    scores = get_text_scores(q_text, v_texts)
    
    if not scores:
        return []
    text_scores = [(v_text, score) for v_text, score in zip(v_texts, scores)]
    scores = sorted(text_scores, key= lambda x: x[1], reverse=True)
    return scores[:k] 