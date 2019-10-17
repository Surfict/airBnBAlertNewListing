FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
COPY config.json config.json
COPY listing.py listing.py
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run"]