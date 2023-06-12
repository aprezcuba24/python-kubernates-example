FROM python:3.8.6-slim

RUN pip3 install --upgrade pip

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app.py ./app.py

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
