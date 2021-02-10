FROM python:3.6-buster
RUN pip3 install --upgrade pip
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install tmux
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-326.0.0-linux-x86_64.tar.gz
RUN 
WORKDIR /mantis_ml
COPY . .
RUN python setup.py install
CMD ["/bin/bash"]


