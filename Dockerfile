# A super-simple "hello world" server that exposes port 8080
#
# VERSION               0.1.0
FROM ubuntu

# create user
RUN groupadd web
RUN useradd -d /home/bottle -m bottle

# make sure sources are up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

# install pip and hello-world server requirements
RUN apt-get -y install python-pip
ADD app.py /home/bottle/app.py
#RUN pip install bottle
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# in case you'd prefer to use links, expose the port
EXPOSE 8080
ENTRYPOINT ["/usr/bin/python", "/home/bottle/app.py"]
USER bottle

