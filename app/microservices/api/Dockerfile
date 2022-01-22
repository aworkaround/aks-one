FROM python:3.10.2-alpine3.14
WORKDIR /app
COPY ./Pipfile .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install pipenv
RUN pip3 install gunicorn
RUN pipenv install --deploy --python /usr/local/bin/python --skip-lock --system

COPY . /app/

ENV DATABASE_URL=sqlite:////app/data.db
ENV SECRET_KEY="87cfb6e9eb4ef60b1b0c5bb2c706ecfa79a9e9dcb6cd057b1337612953490853"

ENTRYPOINT ["gunicorn", "-w", "4", "run:app"]