FROM python:3.7-stretch

RUN apt-get update
RUN apt-get -y upgrade

RUN mkdir opt/playvox
WORKDIR opt/playvox

# Copying the source code CWD
RUN mkdir src
COPY /src src/
COPY entry_point.sh .

RUN mkdir conf

RUN chmod 700 entry_point.sh

ENTRYPOINT ["/opt/playvox/entry_point.sh"]
