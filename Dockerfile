# Base Image
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#RUN pip install --upgrade pip

WORKDIR /project
COPY requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]