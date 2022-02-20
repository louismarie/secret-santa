FROM python:3.7-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /opt/app

COPY requirements.txt .
COPY start-server.sh .
COPY back ./back
COPY api ./api
COPY manage.py .

RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache

RUN mkdir -p /opt/app/back/api/static/
RUN python manage.py collectstatic --noinput

RUN chown -R www-data:www-data /opt/app


EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
