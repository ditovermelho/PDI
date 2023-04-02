FROM python:3.10.10-alpine
LABEL maintainer="Carlos Daniel <carlosdanielferreira246@gmail.com>"
COPY . /Aula03_Lab/pythonfile
WORKDIR /src/pythonfile
EXPOSE 5000
RUN apk update && apk add zlib-dev jpeg-dev gcc musl-dev && python -m pip install --upgrade pip && python -m pip install -r requirements.tx
ENTRYPOINT ["python", "/src/pythonfile/Q_01"]