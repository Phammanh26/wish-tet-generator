from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
version = os.getenv("VERSION", "tetai-0.2.0") 

timeout = os.getenv("TIMEOUT", 20)

# CHATGPT CONNECTION INFO
host = os.getenv("CHATGPT_HOST", None)
token =   os.getenv("CHATGPT_TOKEN", None)

# SERVER INFO
host_server = os.getenv("HOST_SERVER", None)
port_server =   os.getenv("PORT_SERVER", None)



with open("database/general_expections.txt", "r") as f:
        GENERAL_EXPECTIONS = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/ongba/general.txt", "r") as f:
        SPECIAL_ONGBA_EXPECTIONS = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/ongba/ong.txt", "r") as f:
        SPECIAL_ONG_EXPECTIONS = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/ongba/ba.txt", "r") as f:
        SPECIAL_BA_EXPECTIONS = [exp.replace("\n", "") for exp in f.readlines()]


with open("database/bome/bo.txt", "r") as f:
        SPECIAL_BO_EXPECTIONS = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/bome/me.txt", "r") as f:
        SPECIAL_ME_EXPECTIONS = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/general_wish_structure.txt", "r") as f:
        GENERAL_WISH_STRUCTURE = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/end_specical_expections.txt", "r") as f:
        END_SPECIAL_EXPECTIONS  = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/pre_sentence.txt", "r") as f:
        PRE_SENTENCE = [exp.replace("\n", "") for exp in f.readlines()]

with open("database/post_sentence.txt", "r") as f:
        POST_SENTENCE = [exp.replace("\n", "") for exp in f.readlines()]





        