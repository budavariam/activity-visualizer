FROM python:3.6.13 as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
COPY ./*.tar.gz .
RUN pip install --no-cache-dir --prefix=/install --no-warn-script-location -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
WORKDIR /app
RUN mkdir -p logs

COPY ./src ./src
COPY ./assets ./assets
COPY ./logconfig.conf ./logconfig.conf

EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 --log-config /app/logconfig.conf src.app:server