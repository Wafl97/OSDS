FROM ubuntu

# Here, the COPY instruction copies the content of the /L1E3 folder from the host machine to the / (root) destination of the container.
COPY L1E3/ /home/

#Update
RUN apt-get update

#Install python
RUN apt-get install python3 -y

#Run the python script
CMD python3 home/print.py
