FROM python:3.8-slim-buster
RUN apt update && DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y kbd && loadkeys us
RUN apt-get -y install libpq-dev
RUN apt update && apt install tzdata -y
ENV TZ="America/Sao_Paulo"
WORKDIR /app
COPY ./ /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
CMD ["python","-u", "reader.py"]