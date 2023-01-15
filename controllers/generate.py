from controllers.search import GPTSearcher
from loguru import logger
import random
from utils.text import get_text_topk
from utils.processing import post_processing


with open("context/expects/general.txt", "r") as f:
        EXPECTIONS_DEFAULT = [exp.replace("\n", "") for exp in f.readlines()]

with open("context/expects/general_special.txt", "r") as f:
        SPECIAL_EXPECTIONS_DEFAULT = [exp.replace("\n", "") for exp in  f.readlines()]

def generate_expection(expections):
    summary_wish= ["Chúc <NAME>"]
    r_expection = ""
    _expections = []
    for expection in expections:
        expection_results = get_text_topk(expection, EXPECTIONS_DEFAULT, 3)
        print(random.sample(expection_results, 1)[-1][0])
        _expections.extend(random.sample(expection_results, 1)[-1][0])
    print(_expections)
    if _expections == []:
        _expections = random.sample(EXPECTIONS_DEFAULT, 3)
    r_expection = ", ".join(_expections[:-1])
    r_expection += " và " + _expections[-1]
    r_expection += f". {random.sample(summary_wish, 1)[-1]} " + random.sample(SPECIAL_EXPECTIONS_DEFAULT, 1)[-1]
    return r_expection


    

def generate_backup(name, level, expections):
    TETWISH_BACKUP_LIST = []
    
    if level == 'bạn':
        with open("context/friend/sample_wish_tet.txt", "r") as f:
            TETWISH_BACKUP_LIST = f.readlines()
    
    if level == 'anh' or level == 'chị':
        name = f"{level} {name}"
        with open("context/anh_chi/sample.txt", "r") as f:
            TETWISH_BACKUP_LIST = f.readlines()

    if level == 'cô' or level == 'dì'  or level == 'chú'  or level == 'bác' or level == 'thím' or level == 'mợ'  or level == 'cậu':
        name = f"{level} {name}"
        with open("context/co_di_chu_bac/sample.txt", "r") as f:
            TETWISH_BACKUP_LIST = f.readlines()

    result = random.choice(TETWISH_BACKUP_LIST)

    r_expection = generate_expection(expections)
    result = result.replace("<EXPECT>", r_expection)

    result = result.replace("<NAME>", name)
    return result


class TetWishGenerator:
    
    def __init__(self, config, timeout = 30):
        self.config = config
        self.searcher = None
        self.timeout = timeout
        self.set_up(config=config)
        
        
    def set_up(self, config):
        self.searcher = GPTSearcher(
            config = config, 
            timeout = self.timeout
            )
        
        
    def _generate_query(self, name, expections):
    
        ex_context = generate_expection(expections)
        generated_query = f"Tạo câu chúc Tết tới {name}. Những mong muốn của {name}: {ex_context}"
        logger.info(f"Generated query: {generated_query} ")
        return generated_query

    def generate(self, name = "", level = 'bạn', expections = []):
        result  = "Chúc mừng năm mới 2023!"
        try:
            question_query = self._generate_query(name,expections)
            result = self.searcher.search(query_text = question_query)
        
        except Exception as e:
            # generate results backup 
            result = generate_backup(name, level, expections)
            
        result = post_processing(result)
        return result