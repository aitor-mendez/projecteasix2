FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
	build-essential \
	libssl-dev \
	libffi-dev \
	python3-dev \
	curl

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir cryptography
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
