#Use base python
FROM python:3.9-slim

LABEL authors="urijgranickij"

#Install work dir
WORKDIR /app

#Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .  .

#Port
EXPOSE 5000

CMD ["python","app.py"]