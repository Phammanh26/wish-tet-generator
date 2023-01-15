import random
from loguru import logger
import configs
from controllers.search import GPTSearcher
from utils.text import get_text_topk, pharaphase_result, post_processing
from utils.common import listComplementElements


def generate_expection(exp_vocab,  expections, anomalous_level = False):
    r_expection = ""
    _expections = []

    if anomalous_level:
        post_sentence= "<LINKING_WORD> <OWN_LEVEL> chúc <LEVEL_1>"
    else:
        post_sentence= "<LINKING_WORD> <OWN_LEVEL> chúc <NAME> <LEVEL>"
    
    for expection in expections:
        expection_results = get_text_topk(expection, exp_vocab, 3)
        expection_results = listComplementElements(expection_results, _expections)
        _expections.extend([random.sample(expection_results, 1)[-1][0]])
    
    if _expections == [] or len(_expections) < 3:
        _expections.extend(random.sample(exp_vocab, 3 - len(_expections)))

    unique_expections = list(set(_expections))
    r_expection = ", ".join(unique_expections[:-1])
    r_expection += " và " + unique_expections[-1]
    r_expection += f". {post_sentence} " + random.sample(configs.SPECIAL_EXPECTIONS_DEFAULT, 1)[-1]
    return r_expection


    

def generate_backup(name, level, expections):
   
    pre_sentence = ["Tết đến xuân về, ", "2023 đã đến, ", "Nhân dịp đầu xuân, ", "Đầu xuân năm mới, ", "Năm mới đến rồi, ", "Nhân dịp đầu năm mới, ", "Đầu năm, ", "Đầu xuân, ", "Nhân dịp đầu xuân năm mới, ", "Nhân dịp Tết đến xuân sang, "]
    result = ""
    own_level = [""]
    vocab = []
    wish_tet_list = []
    try:
        if level == 'bạn':
            own_level.extend(["mình", "tớ", "tui", "tôi"])
            wish_tet_list = configs.FRIEND_BACKUP_LIST
        
        elif level in ['anh', 'chị']:
            own_level.extend(["em"])
            name = f"{level} {name}"
            wish_tet_list = configs.ANH_CHI_BACKUP_LIST

        elif level in ['cô', 'dì', 'chú', 'bác','thím', 'mợ' , 'cậu']:
            name = f"{level} {name}"
            own_level.extend(["cháu"])
            wish_tet_list =  configs.COCHU_BACKUP_LIST   

        elif level in ['bố', 'mẹ']:
            wish_tet_list =  configs.BO_ME_BACKUP_LIST
            name = level
            own_level.extend(["con"])
            if level == 'bố':
                vocab = [
                "ngày càng phong độ hơn",
                "làm ăn phát tài hơn",
                "kiếm được thật nhiều tiền"
                ]
            else:
                vocab = [
                "hạnh phúc ngập tràn",
                "tươi trẻ hơn",
                "ngày càng khỏe mạnh hơn",
                "luôn luôn tươi trẻ",
                "hạnh phúc bên bố và các con"
                ]
       
        r_expection = generate_expection(expections = expections, exp_vocab= configs.EXPECTIONS_DEFAULT + vocab)
        wish_tet_list = random.choice(wish_tet_list)
        wish_tet_result = f"{random.sample(pre_sentence, 1)[-1]} {wish_tet_list}"
        
    except Exception as e:
        logger.error(e)
        r_expection = generate_expection(
            expections = expections,
            exp_vocab= configs.EXPECTIONS_DEFAULT + vocab,
            anomalous_level = True)
        wish_tet_list = random.choice(configs.BACKUP_LIST)
        wish_tet_result = f"{random.sample(pre_sentence, 1)[-1]} {wish_tet_list}"
    
    pharaphased_result = pharaphase_result(wish_tet_result, name, level, own_level, r_expection)
    result = post_processing(pharaphased_result)
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
            logger.error(e)
            # generate results backup 
            result = generate_backup(name, level, expections)
            
        result = post_processing(result)
        return result