#Use base python
FROM python:3.11-alpine

#Install work dir
WORKDIR app

#Copy dependencies and install them
COPY ./requirements.txt ./requirements.txt

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

CMD ["python","main.py"]