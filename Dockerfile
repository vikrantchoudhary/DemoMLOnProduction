FROM python:3.8.0-slim

COPY ./model.p /

COPY ./requirements.txt /

RUN pip install --no-cache -r requirements.txt

COPY ./app.py /

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]