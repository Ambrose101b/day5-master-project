FROM python:3.9 AS builder

WORKDIR /app

COPY maintenance.py .

FROM python:3.9-slim AS RUNNER

WORKDIR /app

COPY --from=builder /app/maintenance.py .

CMD ["python", "maintenance.py"]