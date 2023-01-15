from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
version = os.getenv("VERSION", "tetai-default:0.0.1") 

# TIMEOUT
timeout = os.getenv("TIMEOUT", 1)

# CHATGPT CONNECTION INFO
host = os.getenv("CHATGPT_HOST", None)
token =   os.getenv("CHATGPT_TOKEN", None)

# SERVER INFO
host_server = os.getenv("HOST_SERVER", None)
port_server =   os.getenv("PORT_SERVER", None)


with open("context/expects/general.txt", "r") as f:
        EXPECTIONS_DEFAULT = [exp.replace("\n", "") for exp in f.readlines()]

with open("context/expects/general_special.txt", "r") as f:
        SPECIAL_EXPECTIONS_DEFAULT = [exp.replace("\n", "") for exp in  f.readlines()]

with open("context/co_di_chu_bac/sample.txt", "r") as f:
        COCHU_BACKUP_LIST = f.readlines()

with open("context/friend/sample_wish_tet.txt", "r") as f:
        FRIEND_BACKUP_LIST = f.readlines()

with open("context/anh_chi/sample.txt", "r") as f:
        ANH_CHI_BACKUP_LIST = f.readlines()

with open("context/bo_me/sample.txt", "r") as f:
        BO_ME_BACKUP_LIST = f.readlines()

with open("context/backup_sample.txt", "r") as f:
        BACKUP_LIST = f.readlines()