FROM python:3.6-buster
RUN pip3 install --upgrade pip
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install tmux
WORKDIR /mantis_ml
COPY . .
RUN python setup.py
CMD ["/bin/bash"]


