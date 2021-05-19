FROM python:3.6-stretch

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV FLASK_APP=manage.py \
    FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000
COPY . .
CMD ["flask", "run"]