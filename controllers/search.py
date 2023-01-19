import json
from loguru import logger
import requests
import re

class GPTSearcher:
    def __init__(self, config):
        self.host = None
        self.token = None
        self.timeout = int(config.timeout)
        self.setup(config)

    def setup(self, config):
        self.host = config.host
        self.token = config.token
        logger.info(f"host = {self.host}, token = {self.token}, timeout = {self.timeout}")
        
    def _search(self, query_text):
        result_search = ""            
        if self.host == None or self.token == None:
            raise NameError(f"Error: host = {self.host} and token = {self.token}")
        else:  

            hed = {'Authorization': 'Bearer ' + self.token}
            data = {"model": "text-davinci-003",
                        "prompt": query_text,
                        "max_tokens": 500,
                        "temperature": 0.5
                        }
            url =  self.host
            rs = requests.post(
                        json= data,
                        timeout=self.timeout, 
                        url=url, 
                        headers=hed
                        )
   
            if rs.status_code == 200:
                result_search = json.loads(rs.content)["choices"][0]["text"][2:]  
            else:
                raise(ValueError("Error response from GPT CORE"))
        return result_search

    def search(self, query_text):
        result = ""
        _result = self._search(query_text)
        match = re.search('[c|C]húc(.+?)*', _result)
        if match:
            result = str(match.group(0))
        return result