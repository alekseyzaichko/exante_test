FROM node:alpine as build-deps

WORKDIR /app/

COPY frontend/package.json frontend/package-lock.json /app/
RUN npm install

COPY frontend /app/
RUN npm run build

FROM nginx:alpine

COPY nginx/prod.conf /etc/nginx/nginx.conf
COPY --from=build-deps /app/dist/ /dist/

CMD ["nginx", "-g", "daemon off;"]