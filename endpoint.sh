
# script to run the server
## run server
kill -9 $(lsof -t -i:8000)
#uvicorn server:app --reload --host 0.0.0.0 --port 8000

uvicorn app.main:app --reload --host 0.0.0.0  --port 8000
