# FROM localhost:5000/alpine:latest
FROM nginx:alpine

WORKDIR /etc/nginx
COPY ./nginx.conf ./conf.d/default.conf
EXPOSE 80
ENTRYPOINT [ "nginx" ]
CMD [ "-g", "daemon off;" ]
