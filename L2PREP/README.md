# PREP
## Docker Compose

Python script:
```py
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
```


Dockerfile:
```Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

Includes in the dir is also a txt file called 'requirements', this file is used to install all the requirements in the image:
```
flask
redis
```


docker-compose:
```yml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
        - .:/code
    environment: 
        FLASK_ENV: development
  redis:
    image: "redis:alpine"
```
The 2 'sevices' are 2 different images

Run the docker-compose.yml (for this im using PowerShell):
- Fist go to the correct dir
```powershell
cd OSDS/OSDS/L2PREP
```
- Then run the file
```
docker-compose up
```
This compiles 2 images and runs them both, the result is a 'web' and 'redis' image.

The result can be seen at:
```http
http://localhost:5000
```

Here i am also useing 'volumes' as part of the 'web' image, which stores binary data on the host machine. In order to remove this data the following command can be used:
```powershell
docker-compose down --volumes
```