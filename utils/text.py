from fuzzywuzzy import fuzz
import random
import re
from controllers.personalize import PersonalWisher

def fix_error_gpt(result, level):
    result = result.replace(f"sẽ được", "sẽ có được")
    result = result.replace(f"luôn được", "sẽ có được")
    result = result.replace(f"May {level}", f"Mong {level}")
    result = result.replace(f"anh/chị", f"{level}")
    result = result.replace(f"May {level}", f"Mong {level}")
    result = result.replace(f"hạnh phúc bền vững", f"Hạnh phúc tràn đầy")
    result = result.replace(f"để yêu đời", f"luôn luôn yêu đời")
    result = result.replace(f"khỏe mạnh mẽ", f"khỏe mạnh")
    result = result.replace(f"của tôi", f"của mình")
    
    
    return result


def pharaphase_search_result(result, personlize_wish: PersonalWisher):
    result = fix_error_gpt(result, personlize_wish.level)
    result = result.replace("Chúc mừng năm mới,", "")
    result = result.replace("bạn", random.sample(personlize_wish.nature_names, 1)[0])
    if personlize_wish.level != "mọi người":
        result = result.replace("mọi người", random.sample(personlize_wish.nature_names, 1)[0])
    result = result.replace("Chúc", "chúc")
    return result

def get_text_scores(q_text, v_texts):
    q_text = q_text.replace('\n', ' ').lower()
    v_texts = [v_text.replace('\n', ' ').lower() for v_text in v_texts]
    scores = [fuzz.partial_ratio(q_text, v_text) for v_text in v_texts]
    return scores

def get_text_topk(q_text, v_texts, k=5):
    outputs = []
    
    scores = get_text_scores(q_text, v_texts)
    if not scores:
        return []
    
    text_scores = [(v_text, score) for v_text, score in zip(v_texts, scores)]
    scores = sorted(text_scores, key= lambda x: x[1], reverse=True)
    
    for s in scores[:k] :
        outputs.append(s[0])
    return outputs


def pharaphase_result(result, personlize_wish: PersonalWisher): 
    
    if personlize_wish.level == "gia đình":
        result = result.replace("<NAME> và", "")
        result_ = result.split(". ")
        result = ". ".join(result_[:-1])
    
    result = result.replace("<NAME>", random.sample(personlize_wish.nature_names, 1)[0])
    result = result.replace("<OWN_LEVEL>", personlize_wish.own_level)
    result = add_icon(result)
    return  result


def add_icon(text):
    icons = ["", "🎉","🙂", "😀", "😄", "😊", "🤑", "🤓", "☘", "🍀", "🍃", "❤", "💕", "💞", "💓", "💗", "💖", "💘", "💝", "💟", "❣", "💕", "💞", "💓", "💗", "💖", "💘", "💝", "💟", "💜", "💛", "❣", "💰", " 💵", "💲", "🌟", "⭐", "🌟", "✨", "💷", "💶", "💴", "💵", "💸", "💪"]
    texts = text.split(". ")
    _texts = []
    _num_duplicates = [0,1,2,3]
    for text in texts:
        if text[-1] not in  [".", "!"]:
            _num = random.sample(_num_duplicates, 1)[0]
            _num_duplicates.remove(_num)
            _texts.append(text + "".join([random.choice(icons)]*_num))
        else:
            _texts.append(text)
    texts = _texts 
    return ". ".join(texts)


def pre_processing(text):
    pass


def upper_first_char(text):
    return text[0].upper() + text[1:]

def post_processing(text):
    # tạo đoạn văn formal or not?
    text = text.replace("\n", "")
    text = re.sub(' +', ' ', text)
    text = text.replace(f"\"", f"")
    text = text.replace(f"\\", f"")
    text = text.replace(f"!.", f".")
    text = text.replace(f"..", f".")
    text = text.replace(f"  ", f" ")
    if text[-1] not in  [".", "!"]:
        text = text + "."
    text = '. '.join(map(lambda s: upper_first_char(s), text.split('. ')))
    return text

def pharaphase_wishing_text(text):    
    pass