FROM python:3.6-alpine

# Refer to https://github.com/opencontainers/image-spec/blob/master/annotations.md
LABEL org.opencontainers.image.title="Hub Sensor - XBee Temperature" \
    org.opencontainers.image.description="A basic XBee-based temperature reader" \
    org.opencontainers.image.authors="Duncan Dickinson" \
    org.opencontainers.image.created="2019" \
    org.opencontainers.image.licences="BSD-2-Clause" \
    org.opencontainers.image.vendor="https://github.com/weather-balloon/" \
    org.opencontainers.image.source="https://github.com/weather-balloon/hub-sensor-xbee-temp" \
    org.opencontainers.image.url="https://github.com/weather-balloon/hub-sensor-xbee-temp" \
    org.opencontainers.image.documentation="https://github.com/weather-balloon/hub-sensor-xbee-temp"

WORKDIR /app

RUN pip install pipenv

COPY test-app/* /app/

RUN pipenv install

ENTRYPOINT [ "pipenv", "run", "python"]

CMD ["sensor.py"]
