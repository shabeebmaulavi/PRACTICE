FROM python:3.11-slim
WORKDIR /app
COPY shabby.py .
CMD ["python", "shabby.py"]