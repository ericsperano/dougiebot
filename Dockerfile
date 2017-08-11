FROM python:alpine

RUN mkdir -p /usr/src/dougiebot

COPY . /usr/src/dougiebot

WORKDIR /usr/src/dougiebot

RUN python setup.py test
RUN pip install .

RUN rm -rf /usr/src/dougiebot

WORKDIR /
ENV PYTHONUNBUFFERED 1

CMD ["/usr/local/bin/dougiebot"]
