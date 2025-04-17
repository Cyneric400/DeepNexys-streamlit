FROM ubuntu:latest
LABEL authors="write"

ENTRYPOINT ["top", "-b"]