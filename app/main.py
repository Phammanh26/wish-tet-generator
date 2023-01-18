# AI CORE
from controllers.generate import TetWishGenerator

# UTILS
import configs
from loguru import logger

# API
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import Depends
from typing import List, Dict
from pydantic import BaseModel
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi.responses import PlainTextResponse
import logging

# Start server
app = FastAPI(host = configs.host_server, port = configs.port_server)
# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set limit request
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Setup logging
handler = logging.FileHandler(filename='logs/file_log.log')
logger.add(handler)

# generator module
tetwish_generator = TetWishGenerator(config = configs, timeout=configs.timeout)


def get_info():
    version = configs.version
    return {"version": f"{version}"}

class CustomForm(BaseModel):
    level: str
    name: str
    expections:  List[str]

@app.post("/generator/TetAI/new")
@limiter.limit("10/minute")
async def tet_generate(data: CustomForm, request: Request):
    # generated_results = tetwish_generator.generate(data.name, data.level, data.expections)
    generated_results ="test"
    return {
        "status": "success",
        "error": {
        },
        "msg":generated_results
    } 
