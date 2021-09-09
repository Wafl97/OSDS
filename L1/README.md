# L1

## E1

Commands run:
```powershell
docker run hello-world
```

## E2

Dockerfile:
```Dockerfile
# A Dockerfile often begins with the FROM instruction, telling the Docker engine which image this image is built from.
# In this case ubuntu is used as the argument.
FROM ubuntu

# The RUN instruction is an instruction that takes a BASH command as an argument. In this way simple functionality is included in the Dockerfile.
# In this case, the text “Hello, World!” is inserted into a txt-file called ‘helloWorld’.
RUN echo “Hello, World! 42.” > helloWorld.txt

# The CMD instruction is the instruction that determines the container's lifetime. This instruction is not runned when building the image. When a container is spinned up from an image, the following command is runned as the executing command. When the command finishes its execution, the container will shut down.
# In this case, the text inside the ‘helloWorld.txt’-file is printed to the screen.
CMD cat helloWorld.txt
```

Commands run:
```powershell
docker build -t L1E2 ./L1E2

docker run L1E2
```

## E3

Initial Dockerfile:

```Dockerfile
FROM ubuntu

COPY L1E3/ /home/

CMD bash
```

Edited Dockerfile:
```Dockerfile
FROM ubuntu

# Here, the COPY instruction copies the content of the /L1E3 folder from the host machine to the / (root) destination of the container.
COPY L1E3/ /home/

#Update
RUN apt-get update

#Install python
RUN apt-get install python3 -y

#Run the python script
CMD python3 home/print.py
```

Commands run:

Before editing the 'Dockerfile'
```powershell
docker build -t L1E3 ./L1E3

docker run -it L1E3
```
*Remember the included folder

After editing the 'Dockerfile'
```powershell
docker build -t L1E3 ./L1E3

docker run L1E3
```

## E4

Dockerfile:
```Dockerfile
FROM php:7.2-apache

COPY ./L1E4 /var/www/html

RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf
```


Commands run:
```powershell
docker build -t L1E4 ./L1E4

docker run -p 80:80 L1E4
```
*Remember the included folder

## E5

Python script:
```py
for i in range(0,10):
    print(":)")
```

Dockerfile:
```Dockerfile
FROM ubuntu

# Here, the COPY instruction copies the content of the /L1E5 folder from the host machine to the / (root) destination of the container.
COPY L1E5/ /home/

#Update
RUN apt-get update

#Install python
RUN apt-get install python3 -y

#Run the python script
CMD python3 home/script.py
```

Commands run:
```powershell
docker build -t L1E5 ./L1E5

docker run L1E5
```
*Remember the included folder

## E6

### Explain what a Dockerfile is.
- A file containing the instructions used to build an image
### How does it work?
- A Dockerfile is compiled(build) to an image, which is a blueprint used to contruct a container when the image is run.
### Which instructions can be used?
- FROM
- RUN
- COPY
- CMD
### What do the above-mentioned instructions do?
- FROM  :   Tells the file what image is being build from
- RUN   :   Takes a bash command and runs it 
- COPY  :   Copies a file into the container when run
- CMD   :   Determins the lifetime of the container, when the CMD is executed the container shuts down
### Explain how a Docker image is built.
- An image is made from a Dockerfile by calling 'build'
### Which options do you know?
- docker build -t <TAG> <DIR-PATH>
- docker build -f <FILE-NAME> <DIR-PATH>
### What are they used for?
- -t    :   Gives the image a handle, used to call it later
- -f    :   Used to specify the name of the Dockerfile, if it is not called 'Dockerfile'
### Explain how a Docker container is runned.
- docker run <TAG>
### Which options do you know?
- -it
### What are they used for?
- -it   :   This tell docker that it is an iterative procces, so you can interact with the container
### Compare cheat sheets and share your pearls of wisdom.
-
