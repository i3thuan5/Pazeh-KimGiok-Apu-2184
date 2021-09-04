FROM python:3.8

WORKDIR /django
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .
RUN cat ./docker/tsuki.py >> ./pazehsite/settings.py

EXPOSE 8000
CMD python manage.py collectstatic --no-input && \
  gunicorn \
  -b 0.0.0.0:8000 \
  --workers 2 --threads 4 \
  --timeout 120 \
  --log-level debug \
  pazehsite.wsgi
