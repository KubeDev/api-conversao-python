FROM python:3.7.3-slim
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt
COPY . .
EXPOSE 5000
RUN chmod 777 ./gunicorn_starter.sh
ENV LOG_FILE="/app/application.log"
CMD ["./gunicorn_starter.sh"]
