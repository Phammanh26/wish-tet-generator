from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
version = "edu-gpt:0.0.1"

# RUNTIME
timeout = 1

# CHATGPT CONNECTION INFO
host = os.getenv("CHATGPT_HOST", None)
token =   os.getenv("CHATGPT_TOKEN", None)

# SERVER INFO
host_server = os.getenv("HOST_SERVER", None)
port_server =   os.getenv("PORT_SERVER", None)