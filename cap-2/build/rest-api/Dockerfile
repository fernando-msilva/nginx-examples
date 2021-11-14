FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uwsgi", "--http", ":8080", "--wsgi-file","api.py"]
EXPOSE 8080