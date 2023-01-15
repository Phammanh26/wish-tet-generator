import json
from loguru import logger
import requests

class GPTSearcher:
    def __init__(self, config, timeout = 30):
        self.host = None
        self.token = None
        self.timeout = timeout
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
            data = {"prompt": query_text}
            url =  self.host
            rs = requests.post(
                        json= data,
                        timeout=self.timeout, 
                        url=url, 
                        headers={
                            "secret_key": self.token
                            }
                        )
            
            if rs.status_code == 200:
                content = json.loads(rs.content)
                if "response" in content:
                    result_search = content["response"] 
                    
            else:
                raise(ValueError("Error response from GPT CORE"))
        return result_search

    def search(self, query_text):
        results = []
        results = self._search(query_text)
        return results