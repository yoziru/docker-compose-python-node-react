FROM node:12-slim
MAINTAINER yoziru

ARG NODE_ENV=development

ENV NODE_PATH=/srv/app/node_modules
WORKDIR /srv/app
COPY yarn.lock package.json ./

RUN set -ex; \
  if [ "$NODE_ENV" = "production" ]; then \
    yarn install --no-cache --frozen-lockfile --production; \
  else \
    yarn install --no-cache --frozen-lockfile; \
  fi;

COPY . /srv/app

EXPOSE 3000
EXPOSE 35729

CMD ["yarn", "run", "start"]
