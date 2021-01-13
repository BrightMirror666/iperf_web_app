FROM ubuntu 
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y iperf3


WORKDIR /app
ADD . /app
RUN pip3 install -r requierements.txt

ENTRYPOINT flask run --host=0.0.0.0 