FROM python:3.8.6

# Copy local code to the container image.
ENV APP_HOME /srv/app
WORKDIR $APP_HOME

# Install production dependencies.
RUN pip install -U pip==20.1.1 setuptools==47.1.1 poetry==1.0.5
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

# disable virtualenv, install dependencies in system python
RUN poetry config virtualenvs.create false
RUN poetry install

# Copy local code to the container image.
COPY . .

# Run the web service on container startup.
EXPOSE 8000
CMD exec python -m src.server
