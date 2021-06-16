FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ${WORKDIR}
RUN pip install -r requirements.txt