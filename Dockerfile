FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
  util-linux \
  e2fsprogs \
  sleuthkit \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY *.py /app/

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/app/generate_forensic_image.py", "-s LucaDomene"]
