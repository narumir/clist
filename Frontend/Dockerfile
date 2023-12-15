FROM nginx:1.24-alpine

WORKDIR /usr/src/app

COPY build .
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
