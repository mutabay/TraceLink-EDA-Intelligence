FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY app/ app/
COPY scripts/ scripts/

RUN pip install --no-cache-dir .

EXPOSE 5000

CMD ["flask", "--app", "app.dashboard.app", "run", "--host", "0.0.0.0", "--port", "5000"]
