FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev

WORKDIR /iciglobal-be

COPY requirements.txt /iciglobal-be/.
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# RUN source /opt/venv/bin/activate

RUN pip install -r requirements.txt --no-cache-dir

COPY . /iciglobal-be/
COPY ./start_server.sh ./strat_server.sh

RUN chmod 777 ./strat_server.sh

CMD [ "python manage.py runserver 0.0.0.0:8000" ]