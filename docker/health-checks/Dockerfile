FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get autoremove -y \
    && apt-get autoclean \
    && apt-get -y install python3 python3-pip \
    && pip3 install discord.py python-dotenv credmgr BotUtils \
    && adduser --home /home/gollum --disabled-password --gecos "Gollum Gollum" gollum

USER gollum
ENV  USER=gollum HOME=/home/gollum
WORKDIR /home/gollum

COPY setup-scripts/*.py ./

# TODO We need to figure out a way to access the log files in the Sia container
#  from this container. We cannot use docker for that.

# NOTE This container expects to be run with
# "-v /home/user/skynet-webportal/.env:/home/gollum/.env"

CMD ["/usr/bin/python3", "./checks-runner.py"]
