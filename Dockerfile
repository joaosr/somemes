FROM django:onbuild
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>

RUN python manage.py migrate

