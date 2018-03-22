# docker-compose-python-node-react

This repo is built as a simple boilerplate to deploy a React front-end app with a Python backend api and a Postgres database using docker-compose.

Start an application with a Python Sanic backend using a postgres database and node.js React frontend, deploy with Docker quickly.

## Requirements

* Docker 1.12.0+

## Setup

To get started, run the following commands in shell.

1.  Build the docker images with docker-compose

    ```
    make build
    ```

    This will build the `frontend` and `backend` images

2.  Start docker-compose containers with the images

    ```
    make up
    ```

    This will start 3 docker containers:

    * `db`: a Postgres 10.x database
    * `backend`: a bare-bone Python Sanic backend API with `asyncpg` to connect to the database
    * `frontend`: a `node.js` 8.x development server with the React front-end (based on `create-react-app`) that talks with the `backend` through a proxy

    Both the frontend and backend support live reload on changes.

## Usage

A `Makefile` is provided with easy to use commands:

### `make up`

Starts the docker-composed containers for the frontend, backend and database

### `make down`

Shuts down the docker-composed containers

### `make build`

Build the docker image for `frontend` and `backend`

### `make backend_bash`

Provides an interactive bash shell into the Python `backend`

### `make frontend_bash`

Provides an interactive bash shell into the node.js `frontend`

## LICENSE

[The MIT License](LICENSE)
