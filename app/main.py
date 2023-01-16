# AI CORE
from controllers.generate import TetWishGenerator

# UTILS
import configs
from loguru import logger

# API
from fastapi import FastAPI
from fastapi.param_functions import Depends
from typing import List, Dict


import logging

# Start server
app = FastAPI(host = configs.host_server, port = configs.port_server)

# Setup logging
handler = logging.FileHandler(filename='logs/file_log.log')
logger.add(handler)

from pydantic import BaseModel

app = FastAPI()



# generator module
tetwish_generator = TetWishGenerator(config = configs, timeout=configs.timeout)

@app.get("/")
def get_info():
    version = configs.version
    return {"version": f"{version}"}



class CustomForm(BaseModel):
    level: str
    name: str
    expections:  List[str]

@app.post("/generator/TetAI/new")
def tet_generate(data: CustomForm):
    generated_results = tetwish_generator.generate(data.name, data.level, data.expections)
    return {
        "status": "success",
        "errors": {
        },
        "msg":generated_results
    } 
