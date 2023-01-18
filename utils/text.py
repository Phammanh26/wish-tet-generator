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


def pharaphase_result(result, name, level):
    print(f"result: {result}")
    own_level = [""]
    if level == 'bạn':
        own_level.extend(["mình", "tớ", "tui", "tôi"])
        result = result.replace("<NAME>", random.choice([name, level]))
        result = result.replace("<LEVEL>", random.choice([name, level]))
        
    elif level in ['anh', 'chị']:
        own_level.extend(["em"])
        result = result.replace("<LEVEL>", level)
        result = result.replace("<NAME>", f"{level} {name}")

    elif level in ['cô', 'dì', 'chú', 'bác','thím', 'mợ' , 'cậu']:
        name = f"{level} {name}"
        own_level.extend(["cháu"])
        result = result.replace("<NAME>", f"{level} {name}")
        result = result.replace("<LEVEL>", random.choice([f"{level} {name}", f"{level}"]))

    elif level in ['bố', 'mẹ']:
        name = level
        own_level.extend(["con"])
        result = result.replace("<NAME>", f"{level}")
        result = result.replace("<LEVEL>", level)
    else:
        result = result.replace("<NAME>", f"{level}")
        result = result.replace("<LEVEL>", level)

    result = result.replace("<LINKING_WORD>", random.choice(["Đặc biệt,", "Đặc biệt hơn,", "Một điều nữa,"]))
    result = result.replace("<LEVEL_1>", level)
    result = result.replace("<OWN_LEVEL>", random.choice(own_level))
    result = result.replace(f"{level} {level}", level)
    result = result.replace(f"{name} {name}", name)
    result = result.replace(f"sẽ được", "sẽ có được")
    result = result.replace(f"luôn được", "sẽ có được")
    result = result.replace(f"May {level}", f"Mong {level}")
    result = result.replace(f"May {level}", f"Mong {level}")
    result = result.replace(f"!.", f".")
    result = result.replace(f"..", f".")
    
    result = result.replace(f"hạnh phúc bền vững", f"Hạnh phúc tràn đầy")
    result = result.replace(f"để yêu đời", f"luôn luôn yêu đời")
    

    
    
    return  result

def pre_processing(text):
    pass


import re
def post_processing(text):
    # tạo đoạn văn formal or not?
    text = text.replace("\n", "")
    text = re.sub(' +', ' ', text)
    return text

def pharaphase_wishing_text(text):
    # tạo đoạn văn formal or not?
    
    pass