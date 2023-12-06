FROM python:3.9

WORKDIR /code

COPY ./requirements.txt ./requirements-dev.txt /code/

RUN pip install --no-cache-dir --upgrade \
    -r /code/requirements.txt \
    -r /code/requirements-dev.txt

COPY ./src /code/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
