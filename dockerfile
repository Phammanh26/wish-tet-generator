# Use a base image with a compatible OS
FROM python:3.9 as build

WORKDIR /code
COPY requirements.txt /code/requirements.txt

RUN pip install --upgrade -r /code/requirements.txt 

COPY . . 

# Use a base image with the same version of Python
FROM python:3.9
WORKDIR /code
COPY --from=build /code /code

RUN pip install --upgrade -r /code/requirements.txt 

# RUN pip install uvicorn
# RUN echo $PATH
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]