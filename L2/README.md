# L2

## E1

Commands run:
```powershell
docker run -p 7000:80 cocodolan/php:apache
```

## E2

```dockerfile
FROM php:apache

RUN docker-php-ext-install mysqli

COPY ./L2E2 /var/www/html
```
* Remember the inculded folder

Commands run:
```powershell
docker build -t l2e2 ./E2

docker run -p 7000:80 l2e2
```

The result can be seen at:
```http
http://localhost:7000
```

## E3

Commands run:

Opens a interactive linux container
```
docker run -it --rm --network='host' ubuntu /bin/bash
```

When in the container:
```bash
apt-get update

apt-get install mysql-server -y

mysql_secure_installation

service mysql start

mysql -u root -p

show databases;

show tables;
```
* 'mysql_secure_installation' requieres some more inputs

After opening mysql:

```SQL
CREATE DATABASE testdb;

CREATE TABLE tTable (data VARCHAR(10));

INSERT INTO tTable (data) VALUE ('ABC');

SELECT * FROM tTable;

DELETE FROM tTable WHERE data='ABC';
```

## E4

Dockerfile:

```dockerfile
FROM mysql

ENV MYSQL_ALLOW_EMPTY_PASSWORD yes

COPY ./L2E4 /docker-entrypoint-initdb.d/.
```
* Remember the included folder.

Commands run:

Fist terminal:
```powershell
docker build -t l2e4 ./E3

docker run l2e4
```

Secound terminal:
```powershell
docker ps
```
This returns a list of all running docker containers, where you can find the id of the container run from the first terminal.

In this case the id was: `a94f38a07b8a`

Now we can use the <i> exec </i> command with the id to access the container from the other terminal.

```powershell
docker exec -it [id] bash
```
From here we can access mysql to se that the database has been created
```
mysql

show databases;
```

## E5

Dockerfile:

Here are both the Dockerfiles from E2 and E4 used in the SQL and WEB dirs respectively, with the included folders.

docker-compose:
```yml
version: '3'
services: 
  db_container:
    build: ./SQL/
    command: --default-authentication-plugin=mysql_native_password
  web_container:
    build: ./WEB/
    depends_on: 
    - db_container
    ports:
    - '7000:80'
```

Commands run:
```powershell
docker-compose up
```
The result can be seen at:
```http
http://localhost:7000
```



