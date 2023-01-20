import configs
import random
import logging
logger = logging.getLogger(__name__)

class PersonalWisher():
    def __init__(self, name, level, taker_expections):
        self.name = name
        self.level = level
        
        self.gender = ""
        self.own_level = ""
        self.nature_names = []
        self.taker_expections = taker_expections
        self.general_expections = []
        self.special_expections = []
        self.setup()
    
    def setup(self):
        self._make_personalize()
        self.general_expections  = configs.GENERAL_EXPECTIONS
    
    def _make_personalize(self):
        
        self.nature_names = [self.level]
        self.own_level = [""]
        self.own_level = ""
        self.special_expections = configs.GENERAL_EXPECTIONS

        if self.level in ['ông', 'bà']:
            _list_own_level = ["cháu", "con"]
            self.own_level = random.sample(_list_own_level, 1)[0]
            self.special_expections = configs.SPECIAL_ONGBA_EXPECTIONS + configs.SPECIAL_BA_EXPECTIONS
            

        elif self.level in ['cô', 'dì', 'chú', 'bác','thím', 'mợ' , 'cậu']:
            self.own_level = "cháu"
        
        elif self.level in ['bố', 'mẹ']:
            self.own_level = "con"

            if self.level == 'bố':
                self.special_expections = configs.SPECIAL_BO_EXPECTIONS
            else:
                self.special_expections = configs.SPECIAL_ME_EXPECTIONS

        elif self.level in ['anh', 'chị']:
            _list_own_level = ["em", "iêm", "đứa em này"]
            self.own_level = random.sample(_list_own_level, 1)[0]
            self.nature_names = [f"{self.level} {self.name}", f"{self.level}"]
            
            # if self.level == 'anh':
            #     self.special_expections = configs.SPECIAL_ANH_EXPECTIONS
            # else:
            #     self.special_expections = configs.SPECIAL_CHI_EXPECTIONS
        
        elif self.level in ['em']:
            self.nature_names = [f"{self.level} {self.name}", f"{self.level}", f"{self.name}", "mày", "m"]

        elif self.level in ['bạn']:
            _dict = {
                "tao": ["mày", "m"],
                "bạn": ["mày", "m", self.name],
                "tui": ["bạn", self.name, "ông"],
                "tôi": [self.name, "ông"],
                "mình": [self.name, "bạn", f"{self.level} {self.name}"]
            }
            self.own_level = random.sample(_dict.keys(), 1)[0]
            self.nature_names = _dict[self.own_level]

        elif self.level in ['thầy giáo']:
            self.own_level = "em"
            self.nature_names = ["Thầy"]
            # self.special_expections = configs.SPECIAL_THAYGIAO_EXPECTIONS

        elif self.level in ['cô giáo']:
            self.own_level = "em"
            self.nature_names = ["Cô"]
            # self.special_expections = configs.SPECIAL_COGIAO_EXPECTIONS