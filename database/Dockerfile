FROM mysql:8.0.25

RUN chown mysql: /var/run/mysqld
RUN chmod 700 /var/run/mysqld

ENV MYSQL_ROOT_PASSWORD="P@ssw0rd" \
    MYSQL_DATABASE="singlepage_storage" \
    MYSQL_USER="user_singlepage" \
    MYSQL_PASSWORD="P@ssword"