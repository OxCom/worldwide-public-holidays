FROM python:3-slim

WORKDIR /opt/app

# in case when your company has self signed certifiacte to decription SSL traffic
# due to security rules, you have to inject this certificate to CA certificates
# COPY .docker/cert.pem /etc/ssl/certs/cert.pem
# RUN cat /etc/ssl/certs/cert.pem >> /etc/ssl/certs/ca-certificates.crt
# ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# in case when you have your custom python configuration, you have to add it to the
# container
# COPY .docker/pip.conf /root/.pip/pip.conf

COPY ./src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/app.py ./src/gunicorn_config.py ./

# RUN python app.py

EXPOSE 80

CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"]
