FROM python:3.10-slim

WORKDIR /app
COPY ./app ..
COPY ./serviceAccountKey.json /app/serviceAccountKey.json
RUN pip install fastapi uvicorn firebase-admin pydantic[email]

EXPOSE 8000
EXPOSE 443

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
