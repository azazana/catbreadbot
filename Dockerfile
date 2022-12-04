FROM python:3.10
RUN mkdir /code

COPY requirements.txt /code

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . ./code

WORKDIR /code/

CMD python3 /code/bot/__main__.py