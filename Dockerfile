FROM python:3
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8002
CMD ["python", "service.py"]
