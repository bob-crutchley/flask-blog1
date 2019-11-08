FROM python:2.7
WORKDIR /app
COPY requirements .
RUN pip install -r requirements
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "run.py"]
