import random
import re
from loguru import logger
import configs
from controllers.search import GPTSearcher
from utils.text import get_text_topk, pharaphase_result, post_processing, pharaphase_search_result
from controllers.personalize import PersonalWisher

def genernate_expection(personlize_wish: PersonalWisher):
    r_expection = ""
    expections = []
    for _expection in personlize_wish.taker_expections:
        _expections = get_text_topk(_expection, personlize_wish.general_expections, 3)
        expections.extend(_expections)
    
    if len(list(set(expections))) < 3:
        expections.extend(random.sample(personlize_wish.general_expections, 5 - len(expections)))

    expections = list(set(expections))
    _expections_random = []
    for _expections in expections:
        _expections_random.append(random.sample(_expections.split(" | "), 1)[0])
    r_expection = ", ".join(_expections_random[:-1])
    r_expection += " và " + _expections_random[-1]
    return r_expection

def generate_pre_sentence():
    return random.choice(configs.PRE_SENTENCE)

def generate_post_sentence():
    return random.choice(configs.POST_SENTENCE)


def customize_search_result(result):
    customized_result = ""
    black_list_words = ["Thiên Chúa", "Chúa", "bổ ích"]
    black_list_character = [":"]
    sub_result_list = result.split(". ")
    _results = []
    for rs in sub_result_list:
        if len(re.findall(r"(?=("+'|'.join(black_list_words)+r"))", rs)) == 0 and len(re.findall(r"(?=("+'|'.join(black_list_character)+r"))", rs)) == 0:
            _results.append(rs)
    customized_result += ". ".join(_results)
    return customized_result


class TetWishGenerator:
    
    def __init__(self, config, timeout = 30):
        self.config = config
        self.searcher = None
        self.structure = ""
        self.set_up(config=config)
            
    def set_up(self, config):
        self.searcher = GPTSearcher(
            config = config, 
            )
        self.structure = {
            "PRE_SENTENCE": "",
            "WISH_GENERAL": "",
            "WISH_PERSONAL": "",
            "WISH_PERSONAL_1": "",
            "POST_SENTENCE": ""
        }

    def _generate_query(self, personlize_wish: PersonalWisher): 
        # make more expections from datatbase
        taker_expections = personlize_wish.taker_expections
        special_expections = personlize_wish.special_expections
        _expections = random.sample(special_expections, min(len(special_expections), 3 - len(taker_expections))) + taker_expections
        _expection_query = ", ".join(_expections)
        generated_query = f"Tạo 1 câu chúc Tết {random.sample(personlize_wish.nature_names, 1)[0]}, kỳ vọng có các từ có nội dung: '{_expection_query}'"
        return generated_query

    def _generate_person_wish(self, personlize_wish: PersonalWisher):
        _structure = "<OWN_LEVEL> chúc <NAME> <EXPECT>"
        try:
            question_query = self._generate_query(personlize_wish)
            result = self.searcher.search(query_text = question_query)
            ## parashase result
            result = pharaphase_search_result(result, personlize_wish)            
            if result == "":
                expection = genernate_expection(personlize_wish)
                _structure.replace("<EXPECT>", expection)
            else:
                _structure = f"<OWN_LEVEL> {result}"
        
        except Exception as e:
            logger.error(e)
            _structure = "Chúc mừng năm mới!"
        
        self.structure["WISH_PERSONAL"] = _structure
    
    def _generate_general_wish(self, personlize_wish: PersonalWisher):
        _structure = random.choice(configs.GENERAL_WISH_STRUCTURE)
        expection = genernate_expection(personlize_wish)
        _structure = _structure.replace("<EXPECT>", expection)
        self.structure["WISH_GENERAL"] = _structure

    def _generate_person_wish_1(self, personlize_wish: PersonalWisher):
        _structure = "<LINKING_WORD> <OWN_LEVEL> chúc <NAME> <EXPECT>"
        _structure = _structure.replace(
            "<LINKING_WORD>", 
            random.choice(["Đặc biệt,", "Đặc biệt hơn,", "Một điều nữa,", "Điều nữa,"])
        )
        
        expection = random.choice(configs.END_SPECIAL_EXPECTIONS)
        _structure = _structure.replace("<EXPECT>", expection)
        self.structure["WISH_PERSONAL_1"] = _structure

        
    def auto_generate(self, personlize_wish):
        self.structure["PRE_SENTENCE"] = generate_pre_sentence()
        self.structure["POST_SENTENCE"] = generate_post_sentence()
        self._generate_general_wish(personlize_wish)
        self._generate_person_wish_1(personlize_wish)
        return self.structure["PRE_SENTENCE"] + " " + self.structure["WISH_GENERAL"] + ". " + self.structure["WISH_PERSONAL_1"] + ". " + self.structure["POST_SENTENCE"]
    
    def generate(self, personlize_wish: PersonalWisher):
        resutls = []
        _resutls = []
        try:
            self.structure["PRE_SENTENCE"] = generate_pre_sentence()
            self.structure["POST_SENTENCE"] = generate_post_sentence()
            self._generate_general_wish(personlize_wish)
            self._generate_person_wish(personlize_wish)
            self._generate_person_wish_1(personlize_wish)
            result = self.structure["PRE_SENTENCE"] + " " + self.structure["WISH_GENERAL"] + ". " + self.structure["WISH_PERSONAL"] + ". " + self.structure["WISH_PERSONAL_1"] + ". " + self.structure["POST_SENTENCE"]
            _resutls.append(result)

        except Exception as e:
            logger.error(e)
            result = ["Chúc mừng năm mới!"] * 3 
        
        _resutls.append(self.auto_generate(personlize_wish))
        _resutls.append(self.auto_generate(personlize_wish))

        
        for rs in _resutls:
            pharaphased_result = pharaphase_result(rs, personlize_wish)
            rs = post_processing(pharaphased_result)
            resutls.append(rs)
        return resutls