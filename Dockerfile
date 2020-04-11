FROM python:3.8

RUN pip install pipenv

WORKDIR /flaskapp

COPY ./Pipfile /flaskapp/Pipfile
COPY ./Pipfile.lock /flaskapp/Pipfile.lock

RUN pipenv install --ignore-pipfile

COPY . /flaskapp

ENV SECRET_KEY = os.environ.get("SECRET_KEY")
ENV JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
ENV SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
ENV SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

EXPOSE 5000

CMD [ "python", "main.py" ]
