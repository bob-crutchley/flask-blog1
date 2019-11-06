FROM python:2.7
WORKDIR /app
RUN pip install gunicorn
COPY requirements .
RUN pip install -r requirements
COPY . .
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "application.__init__:app"]
