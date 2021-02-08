FROM python:3.6-buster
RUN pip3 install --upgrade pip
WORKDIR /mantis_ml
COPY . .
RUN python setup.py
CMD ["/bin/bash"]


