FROM node:8-slim
MAINTAINER yoziru-desu

ARG NODE_ENV=development

RUN npm install -g yarn@1.5.1

ENV NODE_PATH=/app/frontend/node_modules

COPY yarn.lock package.json ./

RUN set -ex; \
  if [ "$NODE_ENV" = "production" ]; then \
    yarn install --no-cache --frozen-lockfile --production; \
  elif [ "$NODE_ENV" = "test" ]; then \
    yarn install --no-cache --frozen-lockfile; \
  fi;

COPY . /app/frontend
WORKDIR /app/frontend

EXPOSE 3000
EXPOSE 35729

CMD ["yarn", "run", "start"]
