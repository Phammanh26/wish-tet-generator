# TODO
# https://www.google.com/search?q=dockerfile+fastapi&sxsrf=AJOqlzWi9elQLemyAvWdQDjepLy051vmQQ%3A1673162714194&ei=2m-6Y5G9C-6C2roPm42siAs&ved=0ahUKEwiRkuzpuLf8AhVugVYBHZsGC7EQ4dUDCA8&uact=5&oq=dockerfile+fastapi&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyCAgAEIAEEMsBMggIABCABBDLATIGCAAQFhAeMggIABAWEB4QCjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoKCAAQRxDWBBCwAzoHCAAQsAMQQzoECAAQQ0oECEEYAEoECEYYAFCeBFjxEmCJFWgBcAF4AIAB8QGIAZULkgEFMC41LjOYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp
# 
FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 
COPY . . 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]