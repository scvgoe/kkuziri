FROM ubuntu:14.04
MAINTAINER DAESEONG KIM <scvgoe@gmail.com>

# PostgreSQL
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \
	&& echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update && apt-get install -y \
    python-pip python-dev uwsgi-plugin-python \
    nginx supervisor libpq-dev libffi-dev g++ \
	libssl-dev python-software-properties \
	software-properties-common postgresql-9.3 \
	postgresql-client-9.3 postgresql-contrib-9.3 \
    docker.io cron

COPY nginx/kkuziri.conf /etc/nginx/sites-available/kkuziri.conf
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir /app
COPY kkuziri /app/kkuziri
COPY config.py /app/config.py
COPY wsgi.py /app/wsgi.py
COPY kkuziri.ini /app/kkuziri.ini
COPY requirements.txt /app/requirements.txt
COPY backup.py /app/backup.py
COPY restore.py /app/restore.py
COPY crontab /etc/cron.d/crontab

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor\
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/kkuziri.conf /etc/nginx/sites-enabled/kkuziri.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    && pip install -r /app/requirements.txt \
    && chown -R www-data:www-data /app \
    && chown -R www-data:www-data /var/log \
    && chmod 0644 /etc/cron.d/crontab

EXPOSE 80
EXPOSE 443

CMD ["/usr/bin/supervisord"]
