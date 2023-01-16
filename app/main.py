# AI CORE
from controllers.generate import TetWishGenerator

# UTILS
import configs
from loguru import logger

# API
from fastapi import FastAPI
import logging

# Start server
app = FastAPI(host = configs.host_server, port = configs.port_server)

# Setup logging
handler = logging.FileHandler(filename='logs/file_log.log')
logger.add(handler)

# generator module
tetwish_generator = TetWishGenerator(config = configs, timeout=configs.timeout)

@app.get("/")
def get_info():
    version = configs.version
    return {"version": f"{version}"}


@app.post("/generator/TetAI/new")
def tet_generate(name: str,  level: str, expections: str):
    # log request
    logger.info(f"Request: name = {name}, level = {level}, expections = {expections}")
    expections = expections.split(",")
    generated_results = tetwish_generator.generate(name, level, expections)
    return {
        "status": "success",
        "errors": {
        },
        "msg":generated_results
    } 
