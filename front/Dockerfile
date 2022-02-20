FROM node:16.14.0-stretch-slim as builder

WORKDIR /usr/src/app

COPY tsconfig* .
COPY vite.config.ts .
COPY vue.config.js .
COPY index.html .
COPY package.json .
COPY yarn.lock .
COPY ./src ./src


RUN yarn install --frozen-lockfile && yarn cache clean
RUN yarn build

FROM nginx:alpine as production-build
COPY ./nginx.conf /etc/nginx/nginx.conf

## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy from the stahg 1
COPY --from=builder /usr/src/app/dist /usr/share/nginx/html

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
