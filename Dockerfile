FROM python:3-alpine3.15
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirement.txt
EXPOSE 4555
CMD ["python3","test.py"]