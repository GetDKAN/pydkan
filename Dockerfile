FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir /opt/pydkan
WORKDIR /opt/pydkan
ADD requirements.txt /opt/pydkan/
RUN pip install -r requirements.txt
RUN pip install ipython
ENV PYTHONPATH=${PYTHONPATH:-/opt/pydkan/}
