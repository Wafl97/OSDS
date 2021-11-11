FROM ubuntu:latest

#Copy the C files
COPY ./multitasking/ ./multitasking

#include packages for compiling
RUN apt-get update && apt-get install build-essential -y

#Compile the C files
RUN make -C multitasking -f makefile

CMD bash