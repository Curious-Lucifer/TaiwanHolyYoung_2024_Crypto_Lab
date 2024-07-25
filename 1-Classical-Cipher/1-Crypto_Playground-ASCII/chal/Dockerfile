FROM nginx

RUN mkdir -p /var/www/html

COPY dist/ /var/www/html
COPY conf/nginx.conf /etc/nginx/conf.d/default.conf
