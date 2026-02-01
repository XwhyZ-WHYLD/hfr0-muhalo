FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir ".[all]"
EXPOSE 8000
CMD ["hfr0", "demo", "--port", "8000"]
