from fuzzywuzzy import fuzz
import random

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


def pharaphase_result(result, name, level, own_level, str_expection):
    result = result.replace("<EXPECT>", str_expection)
    result = result.replace("<LINKING_WORD>", random.choice(["Đặc biệt", "Đặc biệt hơn", "Một điều nữa, "]))
    result = result.replace("<NAME>", random.choice([name, level]))
    result = result.replace("<LEVEL>", random.choice([name, level]))
    result = result.replace("<LEVEL_1>", level)
    result = result.replace("<OWN_LEVEL>", random.choice(own_level))

    return  result

def pre_processing(text):
    pass



def post_processing(text):
    # tạo đoạn văn formal or not?
    text = text.replace("\n", "")
    text = text.replace("  ", " ")
    return text

def pharaphase_wishing_text(text):
    # tạo đoạn văn formal or not?
    
    pass