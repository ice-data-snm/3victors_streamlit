# app/Dockerfile

FROM python:3.10-slim

EXPOSE 8501

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "st-app.py", "--server.port=8501", "--server.address=0.0.0.0"]
