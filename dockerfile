FROM python:3.8
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /opt/
WORKDIR /opt
EXPOSE 8000
ENTRYPOINT  uvicorn mall.main:app --host=0.0.0.0 --port=8000