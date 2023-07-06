FROM python:3.9-buster

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/firstProject
RUN mkdir -p /opt/app/pip_cache
COPY req.txt start-server.sh /opt/app/
COPY firstProject /opt/app/firstProject/
WORKDIR /opt/app
RUN pip install -r req.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app
RUN chmod -R 777 /opt/app

EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]


