FROM python:3.11.2-slim

ENV APP_HOME /opt/sonet/
WORKDIR $APP_HOME
ENV PYTHONPATH=/opt/sonet
COPY . $APP_HOME
RUN python -m pip install --upgrade pip && pip install --no-cache-dir pipenv \
    && pipenv install --deploy --system --ignore-pipfile

EXPOSE 8000
