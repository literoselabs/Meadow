FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive

LABEL maintainer="literoselabs@protonmail.com"
LABEL version="0.1"
LABEL description="Custom Docker container for bootstrapping and testing Meadow environment"

COPY . /tmp/meadow
WORKDIR /tmp/meadow

RUN apt update
RUN apt install -y python3-apt python3-pip build-essential git
RUN pip3 install -r requirements.txt

CMD [ "python3", "meadow.py", "bootstrap", "--pxe", "--proxy_dhcp"]